import pygame

class CollisionSystem:
    def __init__(self, level_scene):
        self.level_scene = level_scene

    def handle_projectile_enemy_collision(self, projectiles: pygame.sprite.Group, enemy: pygame.sprite.Group):
        collisions = pygame.sprite.groupcollide(projectiles, enemy, True, False)
        for projectile, enemies in collisions.items():
            for enemy in enemies:
                self.level_scene.on_enemy_hit({"enemy": enemy, "projectile": projectile})
    
    def handle_projectile_player_collision(self, projectiles: pygame.sprite.Group, player: pygame.sprite.Sprite):
        collisions = pygame.sprite.spritecollide(player, projectiles, True)
        for projectile in collisions:
            self.level_scene.on_player_hit({"player": player, "projectile": projectile})

    def handle_projectile_projectile_collision(self, projectiles: pygame.sprite.Group):
        projectile_list = projectiles.sprites()
        for i in range(len(projectile_list)):
            for j in range(i + 1, len(projectile_list)):
                if projectile_list[i].speed_x != projectile_list[j].speed_x and projectile_list[i].rect.colliderect(projectile_list[j].rect):
                    projectile_list[i].kill()
                    projectile_list[j].kill()
                    self.level_scene.on_projectile_hit({"projectile1": projectile_list[i], "projectile2": projectile_list[j]})