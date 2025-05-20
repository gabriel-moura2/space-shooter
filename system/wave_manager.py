from typing import List
import colorsys
import pygame
from entities.enemy_ship import EnemyShip
from config import SCREEN_WIDTH, H_POSITION_PLAYER, SCREEN_HEIGHT, SHIP_SPEED, PROJECTILE_SPEED, PROJECTILE_DAMAGE, HEALTH

class WaveManager:
    def __init__(self, wave_spawn_config: List[List[int]]):
        self.wave_spawn_config = wave_spawn_config
        self.current_wave_index = 0

    def _enemy_create(self, enemy_type: int, index: int, total_enemies: int, projectile_manager: pygame.sprite.Group) -> EnemyShip:
        position = self._calculate_enemy_spawn_position(index, total_enemies)
        enemy = EnemyShip(position, enemy_type, projectile_manager)
        enemy.projectile_config = {
            'damage': PROJECTILE_DAMAGE * ((enemy_type >> 2 & 1) + 1),
            'speed': PROJECTILE_SPEED * ((enemy_type >> 1 & 1) + 1)
        }
        enemy.speed = SHIP_SPEED * ((enemy_type >> 3 & 1) + 1)
        enemy.health = HEALTH * ((enemy_type & 1) + 1)
        enemy.is_double_shot = bool((enemy_type >> 4) & 1)
        pxarray = pygame.PixelArray(enemy.image)
        color1 = 255 - (enemy_type >> 4) * 85, 255 - (enemy_type >> 2 & 3) * 85, 255 - (enemy_type & 3) * 85
        hsv = colorsys.rgb_to_hsv(color1[0] / 255, color1[1] / 255, color1[2] / 255)
        rgb = colorsys.hsv_to_rgb((hsv[0] - (1/9)) % 1, hsv[1], hsv[2] / 3)
        color2 = int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        pxarray.replace((51, 51, 0), color2)
        pxarray.replace((51, 153, 0), color1)
        pxarray.close()
        return enemy
    
    def _calculate_enemy_spawn_position(self, index: int, total_enemies: int) -> tuple:
        return (SCREEN_WIDTH + H_POSITION_PLAYER, SCREEN_HEIGHT * (index + 1) / (total_enemies + 1))
    
    def spawn_next_wave(self, enemies_group: pygame.sprite.Group, projectile_manager: pygame.sprite.Group) -> None:
        if self.current_wave_index >= len(self.wave_spawn_config):
            return

        enemy_types = self.wave_spawn_config[self.current_wave_index]
        self.current_wave_index += 1
        for i, enemy_type in enumerate(enemy_types):
            enemies_group.add(self._enemy_create(enemy_type-1, i, len(enemy_types), projectile_manager))

    @property
    def is_complete(self) -> bool:
        return self.current_wave_index >= len(self.wave_spawn_config)