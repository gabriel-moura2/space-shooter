from typing import List
import pygame
from entities.explosion import ExplosionEffect
from config import SCREEN_WIDTH

class CollisionSystem:
    def __init__(self, explosion_manager: pygame.sprite.Group):
        self.explosion_manager = explosion_manager

    def handle_projectile_enemy_collision(self, projectile: List[pygame.sprite.Sprite], enemy: List[pygame.sprite.Sprite]):
        collisions = pygame.sprite.groupcollide(projectile, enemy, True, False)
        for projectile, enemies in collisions.items():
            for enemy in enemies:
                self._resolve_ship_hit(projectile, enemy)
    
    def handle_projectile_player_collision(self, projectile: List[pygame.sprite.Sprite], player: pygame.sprite.Sprite):
        collisions = pygame.sprite.spritecollide(player, projectile, True)
        for projectile in collisions:
            self._resolve_ship_hit(projectile, player)

    def _resolve_ship_hit(self, projectile: pygame.sprite.Sprite, ship: pygame.sprite.Sprite):
        self.explosion_manager.add(ExplosionEffect(projectile.rect.center, 36))
        ship.hit(projectile.damage)
        if ship.health <= 0:
            self.explosion_manager.add(ExplosionEffect(ship.rect.center, 8))
            ship.kill()
    
    def handle_projectile_bounds(self, projectile: List[pygame.sprite.Sprite]):
        for projectile in projectile:
            if projectile.rect.left < 0 or projectile.rect.right > SCREEN_WIDTH:
                projectile.kill()