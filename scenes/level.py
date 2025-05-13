import pygame
from scenes.scene import Scene
from entities.background import Background
from entities.enemy_ship import EnemyShip
from entities.player_ship import PlayerShip
from config import SCREEN_HEIGHT, SHIP_SPEED, SCREEN_WIDTH

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self.projectiles = []
        self.enemies = [EnemyShip(SCREEN_HEIGHT / 2, 12, self.projectiles)]
        self.player = PlayerShip(self.projectiles)
        self.background = Background()

    def handle_events(self):
        super().handle_events()
        pressed_keys = pygame.key.get_pressed()
        if (pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]):
            self.player.speed = -SHIP_SPEED * 2
        elif (pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]):
            self.player.speed = SHIP_SPEED * 2
        else:
            self.player.speed = 0
        if (pressed_keys[pygame.K_SPACE]):
            self.player.shoot()
    
    def update(self, dt):
        super().update(dt)
        for projectile in self.projectiles:
            if projectile.rect.left < 0 or projectile.rect.right > SCREEN_WIDTH:
                self.projectiles.remove(projectile)
    
    def draw(self, screen):
        super().draw(screen)

    @property
    def entities(self):
        return [self.background, self.player, *self.enemies, *self.projectiles]