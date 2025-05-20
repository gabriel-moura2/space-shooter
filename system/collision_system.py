import pygame
from entities.explosion import ExplosionEffect
from config import SCREEN_WIDTH

class CollisionSystem:
    def __init__(self, explosion_manager: pygame.sprite.Group):
        self.explosion_manager = explosion_manager

    def handle_projectile_enemy_collision(self, projectiles: pygame.sprite.Group, enemy: pygame.sprite.Group):
        collisions = pygame.sprite.groupcollide(projectiles, enemy, True, False)
        for projectile, enemies in collisions.items():
            for enemy in enemies:
                self._resolve_ship_hit(projectile, enemy)
    
    def handle_projectile_player_collision(self, projectiles: pygame.sprite.Group, player: pygame.sprite.Sprite):
        collisions = pygame.sprite.spritecollide(player, projectiles, True)
        for projectile in collisions:
            self._resolve_ship_hit(projectile, player)

    def _resolve_ship_hit(self, projectiles: pygame.sprite.Sprite, ship: pygame.sprite.Sprite):
        self.explosion_manager.add(ExplosionEffect(projectiles.rect.center, 36))
        ship.hit(projectiles.damage)
        if ship.health <= 0:
            self.explosion_manager.add(ExplosionEffect(ship.rect.center, 8))
            ship.kill()

    def handle_projectile_projectile_collision(self, projectiles: pygame.sprite.Group):
        projectile_list = projectiles.sprites()
        for i in range(len(projectile_list)):
            for j in range(i + 1, len(projectile_list)):
                if projectile_list[i].direction != projectile_list[j].direction and projectile_list[i].rect.colliderect(projectile_list[j].rect):
                    projectile_list[i].kill()
                    projectile_list[j].kill()
                    self.explosion_manager.add(ExplosionEffect(projectile_list[i].rect.center, 36))
    
    def handle_projectile_bounds(self, projectiles: pygame.sprite.Group):
        for projectile in projectiles:
            if projectile.rect.left < 0 or projectile.rect.right > SCREEN_WIDTH:
                projectile.kill()