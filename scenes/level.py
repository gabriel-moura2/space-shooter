from typing import Dict
import pygame
import math
from core.scene_manager import SceneManager
from system.input_handler import InputHandler
from system.collision_system import CollisionSystem
from system.wave_manager import WaveManager
from system.explosion_manager import ExplosionManager
from system.projectile_manager import ProjectileManager
from base.scene import Scene
from entities.background import SpaceBackground
from entities.player_ship import PlayerShip
from ui.text import Text
from ui.health import HealthDisplay
from utils.helpers import generate_partitions_dp
from config import H_POSITION_PLAYER, H_POSITION_ENEMY, LEVEL_DISPLAY_CONFIG, SCREEN_HEIGHT, SCREEN_WIDTH

class LevelScene(Scene):
    def __init__(self, manager: SceneManager, input_handler: InputHandler, level: int) -> None:
        super().__init__(manager, input_handler)
        self.level: int = level
        self.wave_manager: WaveManager = WaveManager(generate_partitions_dp(self.level, 7, 63))
        self._init_game_objects()
        self.collision_system: CollisionSystem = CollisionSystem(self)

    def _init_game_objects(self) -> None:
        self.sprite_groups: Dict[str, pygame.sprite.Group] = {
            "enemies": pygame.sprite.Group(),
            "projectiles": ProjectileManager(),
            "player": pygame.sprite.GroupSingle(),
            "health_displays": pygame.sprite.Group(),
            "explosions": ExplosionManager(),
            "ui": pygame.sprite.Group(Text(**LEVEL_DISPLAY_CONFIG, text=f"Level {self.level}"))
        }
        self.background: SpaceBackground = SpaceBackground()
        self.sprite_groups["player"].add(PlayerShip((-H_POSITION_PLAYER, SCREEN_HEIGHT / 2), self.sprite_groups["projectiles"]))
        self.input_handler.attach(self.sprite_groups["player"].sprite)
        self.sprite_groups["health_displays"].add(HealthDisplay(self.sprite_groups["player"].sprite))
    
    def update(self, dt: float) -> None:
        super().update(dt)
        self._update_background(dt)
        self._check_gameover_conditions()
        if self.sprite_groups["player"].sprite:
            self._check_win_conditions()
            self._spawn_enemies_if_needed()
            self._handle_enemy_attacks()
            self._handle_collisions()
    
    def draw(self, screen) -> None:
        self.background.draw(screen)
        super().draw(screen)

    def _update_background(self, dt: float) -> None:
        self.background.update(dt)

    def _handle_enemy_attacks(self) -> None:
        for enemy in self.sprite_groups["enemies"]:
            if enemy.can_rotate:
                dx = enemy.rect.left - self.sprite_groups["player"].sprite.rect.right
                dy = enemy.rect.centery - self.sprite_groups["player"].sprite.rect.centery
                enemy.rotate(dx, dy)
                if enemy.rect.right < SCREEN_WIDTH:
                    enemy.shoot()
            else:
                if self.sprite_groups["player"].sprite.rect.clipline(self._calculate_attack_line(enemy.rect)):
                    enemy.shoot()

    def _calculate_attack_line(self, rect) -> tuple:
        return (rect.centerx - (H_POSITION_ENEMY - H_POSITION_PLAYER), rect.centery, rect.centerx, rect.centery)
    
    def _handle_collisions(self) -> None:
        self.collision_system.handle_projectile_player_collision(self.sprite_groups["projectiles"].projectiles, self.sprite_groups["player"].sprite)
        self.collision_system.handle_projectile_enemy_collision(self.sprite_groups["projectiles"].projectiles, self.sprite_groups["enemies"])
        self.collision_system.handle_projectile_projectile_collision(self.sprite_groups["projectiles"].projectiles)

    def _spawn_enemies_if_needed(self) -> None:
        if len(self.sprite_groups["enemies"]) != 0:
            return

        if self.wave_manager.is_complete:
            self.sprite_groups["player"].sprite.win = True
            return
            
        self.wave_manager.spawn_next_wave(self.sprite_groups["enemies"], self.sprite_groups["projectiles"])
        for enemy in self.sprite_groups["enemies"]:
            self.sprite_groups["health_displays"].add(HealthDisplay(enemy))

    def _advance_to_next_level(self) -> None:
        self.input_handler.detach(self.sprite_groups["player"].sprite)
        if self.level >= 441:
            from scenes.congratulations import CongratulationsScene
            self.manager.change_scene(CongratulationsScene(self.manager, self.input_handler))
            return
        self.manager.change_scene(LevelScene(self.manager, self.input_handler, self.level + 1))

    def _check_win_conditions(self) -> None:
        if self.sprite_groups["player"].sprite.rect.x >= SCREEN_WIDTH + H_POSITION_PLAYER:
            self._advance_to_next_level()

    def _check_gameover_conditions(self) -> None:
        if len(self.sprite_groups["player"]) == 0 and len(self.sprite_groups["explosions"]) == 0:
            from scenes.game_over import GameOverScene
            self.manager.change_scene(GameOverScene(self.manager, self.input_handler, f"#{self.level}.{self.wave_manager.current_wave_index}"))

    def _resolve_ship_hit(self, projectiles: pygame.sprite.Sprite, ship: pygame.sprite.Sprite):
        self.sprite_groups["explosions"].create_explosion(projectiles.rect.center, 36)
        ship.hit(projectiles.damage)
        if ship.health <= 0:
            self.sprite_groups["explosions"].create_explosion(ship.rect.center, 8)
            ship.kill()

    def on_enemy_hit(self, event) -> None:
        self._resolve_ship_hit(event["projectile"], event["enemy"])

    def on_player_hit(self, event) -> None:
        self._resolve_ship_hit(event["projectile"], event["player"])
        if event["player"].health <= 0:
            self.input_handler.detach(event["player"])

    def on_projectile_hit(self, event) -> None:
        self.sprite_groups["explosions"].create_explosion(event["projectile1"].rect.center, 36)