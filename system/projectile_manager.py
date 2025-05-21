import pygame
from entities.projectile import Projectile

class ProjectileManager:
    def __init__(self):
        self.projectiles = pygame.sprite.Group()

    def create_projectile(self, position, direction, damage, speed):
        self.projectiles.add(Projectile(position, direction, damage, speed))

    def update(self, dt):
        self.projectiles.update(dt)

    def draw(self, surface):
        self.projectiles.draw(surface)

    