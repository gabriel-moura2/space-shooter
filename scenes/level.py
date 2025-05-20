from typing import List, Dict
import pygame
from core.scene_manager import SceneManager
from system.input_handler import InputHandler
from system.collision_system import CollisionSystem
from base.scene import Scene
from entities.background import SpaceBackground
from entities.enemy_ship import EnemyShip
from entities.double_shot_enemy_ship import DoubleShotEnemyShip
from entities.player_ship import PlayerShip
from ui.text import Text
from ui.health import HealthDisplay
from utils.helpers import generate_partitions
from config import SCREEN_HEIGHT, H_POSITION_PLAYER, H_POSITION_ENEMY, SCREEN_WIDTH, LEVEL_DISPLAY_CONFIG

class LevelScene(Scene):
    def __init__(self, manager: SceneManager, input_handler: InputHandler, level: int) -> None:
        super().__init__(manager, input_handler)
        self.level: int = level
        self._init_level_structure()
        self._init_game_objects()
        self.collision_system: CollisionSystem = CollisionSystem(self.sprite_groups["explosions"])

    def _init_level_structure(self) -> None:
        self.wave_spawn_config: List[List[int]] = generate_partitions(self.level, 7)
        self.current_wave_index: int = 0

    def _init_game_objects(self) -> None:
        self.sprite_groups: Dict[str, pygame.sprite.Group] = {
            "enemies": pygame.sprite.Group(),
            "projectiles": pygame.sprite.Group(),
            "player": pygame.sprite.GroupSingle(),
            "health_displays": pygame.sprite.Group(),
            "explosions": pygame.sprite.Group(),
            "ui": pygame.sprite.Group(Text(**LEVEL_DISPLAY_CONFIG, text=f"Level {self.level}"))
        }
        self.sprite_groups["player"].add(PlayerShip(self.sprite_groups["projectiles"]))
        self.input_handler.attach(self.sprite_groups["player"].sprite)
        self.sprite_groups["health_displays"].add(HealthDisplay(self.sprite_groups["player"].sprite))
        self.background: SpaceBackground = SpaceBackground()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
    
    def update(self, dt: float) -> None:
        super().update(dt)
        self._update_background(dt)
        self._handle_enemy_attacks()
        self.collision_system.handle_projectile_bounds(self.sprite_groups["projectiles"])
        self._handle_collisions()
        self._spawn_enemies_if_needed()
        self._check_gameover_conditions()
    
    def draw(self, screen) -> None:
        self.background.draw(screen)
        super().draw(screen)

    def _update_background(self, dt: float) -> None:
        self.background.update(dt)

    def _handle_enemy_attacks(self) -> None:
        for enemy in self.sprite_groups["enemies"]:
            if self.sprite_groups["player"].sprite.rect.clipline(self._calculate_attack_line(enemy.rect)):
                enemy.shoot()

    def _calculate_attack_line(self, rect) -> tuple:
        return (rect.centerx - (H_POSITION_ENEMY - H_POSITION_PLAYER), rect.centery, rect.centerx, rect.centery)
    
    def _handle_collisions(self) -> None:
        self.collision_system.handle_projectile_player_collision(self.sprite_groups["projectiles"], self.sprite_groups["player"].sprite)
        self.collision_system.handle_projectile_enemy_collision(self.sprite_groups["projectiles"], self.sprite_groups["enemies"])

    def _spawn_enemies_if_needed(self) -> None:
        if len(self.sprite_groups["enemies"]) == 0:
            if self.current_wave_index >= len(self.wave_spawn_config):
                self._advance_to_next_level()
                return

            enemy_types = self.wave_spawn_config[self.current_wave_index]
            self.current_wave_index += 1
            for i, enemy_type in enumerate(enemy_types):
                enemy_class = DoubleShotEnemyShip if (enemy_type-1) >> 4 & 1 == 1 else EnemyShip
                position = self._calculate_enemy_spawn_position(i, len(enemy_types))
                enemy = enemy_class(position, (enemy_type-1), self.sprite_groups["projectiles"])
                self.sprite_groups["enemies"].add(enemy)
                self.sprite_groups["health_displays"].add(HealthDisplay(enemy))

    def _advance_to_next_level(self) -> None:
        self.manager.change_scene(LevelScene(self.manager, self.input_handler, self.level + 1))

    def _calculate_enemy_spawn_position(self, index: int, total_enemies: int) -> tuple:
        return (SCREEN_WIDTH + H_POSITION_PLAYER, SCREEN_HEIGHT * (index + 1) / (total_enemies + 1))

    def _check_gameover_conditions(self) -> None:
        if len(self.sprite_groups["player"]) == 0:
            from scenes.game_over import GameOverScene
            self.input_handler.detach(self)
            self.manager.change_scene(GameOverScene(self.manager, self.input_handler, f"#{self.level}.{self.current_wave_index}"))