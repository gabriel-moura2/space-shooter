import pygame
from system.level_event_manager import LevelEventManager
from config import SCREEN_WIDTH

class CollisionSystem:
    def __init__(self, level_event_manager: LevelEventManager):
        self.level_event_manager = level_event_manager

    def handle_projectile_enemy_collision(self, projectiles: pygame.sprite.Group, enemy: pygame.sprite.Group):
        collisions = pygame.sprite.groupcollide(projectiles, enemy, True, False)
        for projectile, enemies in collisions.items():
            for enemy in enemies:
                self.level_event_manager.notify("enemy_hit", {"enemy": enemy, "projectile": projectile})
    
    def handle_projectile_player_collision(self, projectiles: pygame.sprite.Group, player: pygame.sprite.Sprite):
        collisions = pygame.sprite.spritecollide(player, projectiles, True)
        for projectile in collisions:
            self.level_event_manager.notify("player_hit", {"player": player, "projectile": projectile})

    def handle_projectile_projectile_collision(self, projectiles: pygame.sprite.Group):
        projectile_list = projectiles.sprites()
        for i in range(len(projectile_list)):
            for j in range(i + 1, len(projectile_list)):
                if projectile_list[i].direction != projectile_list[j].direction and projectile_list[i].rect.colliderect(projectile_list[j].rect):
                    projectile_list[i].kill()
                    projectile_list[j].kill()
                    self.level_event_manager.notify("projectile_hit", {"projectile1": projectile_list[i], "projectile2": projectile_list[j]})