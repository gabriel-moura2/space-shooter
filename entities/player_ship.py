import pygame
from entities.space_ship import SpaceShip
from entities.projectile import Projectile
from utils.helpers import load_image
from config import H_POSITION_PLAYER, SHIP_SPEED, SCREEN_HEIGHT, PROJECTILE_SPEED, PROJECTILE_DAMAGE, HEALTH

class PlayerShip(SpaceShip):
    def __init__(self, projectile_manager):
        super().__init__(load_image("player"), (H_POSITION_PLAYER, SCREEN_HEIGHT / 2), projectile_manager)
        self.health = HEALTH
        self.speed = 0

    def update(self, dt):
        if self.rect.top + self.speed * dt < 0 or self.rect.bottom + self.speed * dt > SCREEN_HEIGHT:
             return
        super().update(dt)

    def shoot(self):
        self.projectile_manager.add(Projectile((self.rect.right, self.rect.centery), 1, PROJECTILE_DAMAGE, PROJECTILE_SPEED))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.shoot()

    def handle_keys(self, pressed_keys):
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.speed = -SHIP_SPEED * 2
        elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.speed = SHIP_SPEED * 2
        else:
            self.speed = 0