import pygame
from entities.space_ship import SpaceShip
from utils.helpers import load_image
from config import H_POSITION_PLAYER, SHIP_SPEED, PROJECTILE_SPEED, PROJECTILE_DAMAGE, HEALTH

class PlayerShip(SpaceShip):
    def __init__(self, position, projectile_manager):
        super().__init__(load_image("player"), position, projectile_manager)
        self.health = HEALTH
        self.speed = 0
        self.win = False

    def update(self, dt):
        if self.rect.x < H_POSITION_PLAYER:
            self.rect = self.rect.move(SHIP_SPEED * 2 * dt, 0)
            return
        if self.win:
            self.rect = self.rect.move(SHIP_SPEED * 3 * dt, 0)
            return
        super().update(dt)
        self.speed = 0

    def shoot(self):
        self.projectile_manager.create_projectile((self.rect.right, self.rect.centery), 0, PROJECTILE_DAMAGE, PROJECTILE_SPEED)

    def handle_input_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.shoot()

    def handle_pressed_keys(self, pressed_keys):
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.speed = -SHIP_SPEED * 2
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.speed = SHIP_SPEED * 2