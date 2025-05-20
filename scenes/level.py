from typing import List, Dict
import pygame
from core.scene_manager import SceneManager
from system.input_handler import InputHandler
from system.collision_system import CollisionSystem
from system.wave_manager import WaveManager
from base.scene import Scene
from entities.background import SpaceBackground
from entities.player_ship import PlayerShip
from ui.text import Text
from ui.health import HealthDisplay
from utils.helpers import generate_partitions
from config import H_POSITION_PLAYER, H_POSITION_ENEMY, LEVEL_DISPLAY_CONFIG

class LevelScene(Scene):
    def __init__(self, manager: SceneManager, input_handler: InputHandler, level: int) -> None:
        super().__init__(manager, input_handler)
        self.level: int = level
        self.wave_manager: WaveManager = WaveManager(generate_partitions(self.level, 7))
        self._init_game_objects()
        self.collision_system: CollisionSystem = CollisionSystem(self.sprite_groups["explosions"])

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
        """
        Updates the scene by calling update on all groups, updating the background,
        making enemies attack, checking collisions, spawning enemies if needed, and
        checking if the game is over.

        Args:
            dt (float): The time elapsed since last update.
        """
        super().update(dt)
        self._update_background(dt)
        self._handle_enemy_attacks()
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
        """ Handle all the collisions in the level scene.

        This method is called in the update method of the LevelScene class. It
        handles the collisions between the player and the projectiles, the
        enemies and the projectiles, and the projectiles among themselves.

        """
        self.collision_system.handle_projectile_player_collision(self.sprite_groups["projectiles"], self.sprite_groups["player"].sprite)
        self.collision_system.handle_projectile_enemy_collision(self.sprite_groups["projectiles"], self.sprite_groups["enemies"])
        self.collision_system.handle_projectile_projectile_collision(self.sprite_groups["projectiles"])

    def _spawn_enemies_if_needed(self) -> None:
        """Spawn the next wave of enemies if there are no more enemies in the level.

        This method is called in the update method of the LevelScene class. It
        first checks if there are any more enemies in the level. If there are, it
        does nothing. If there are no more enemies, it checks if the WaveManager
        has completed its waves. If it has, it calls the _advance_to_next_level
        method to advance to the next level. If it has not, it spawns the next
        wave of enemies and adds their health displays to the game.
        """
        if len(self.sprite_groups["enemies"]) != 0:
            return

        if self.wave_manager.is_complete:
            self._advance_to_next_level()
            return
            
        self.wave_manager.spawn_next_wave(self.sprite_groups["enemies"], self.sprite_groups["projectiles"])
        for enemy in self.sprite_groups["enemies"]:
            self.sprite_groups["health_displays"].add(HealthDisplay(enemy))

    def _advance_to_next_level(self) -> None:
        """Advance to the next level.

        This method is called when the player has defeated all enemies in the
        current level. It detaches the input handler and changes the current
        scene to the next level, passing the current level plus one as the new
        level index.
        """
        self.input_handler.detach(self.sprite_groups["player"].sprite)
        self.manager.change_scene(LevelScene(self.manager, self.input_handler, self.level + 1))

    def _check_gameover_conditions(self) -> None:
        """Check if the game is over and transition to the GameOverScene.

        This method checks if the player's sprite group is empty, indicating
        that the player has been defeated. If so, it detaches the input
        handler and changes the current scene to the GameOverScene, passing
        the current level and wave index as the score.
        """
        if len(self.sprite_groups["player"]) == 0:
            from scenes.game_over import GameOverScene
            self.input_handler.detach(self.sprite_groups["player"].sprite)
            self.manager.change_scene(GameOverScene(self.manager, self.input_handler, f"#{self.level}.{self.wave_manager.current_wave_index}"))