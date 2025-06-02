import pygame
from entities.explosion import ExplosionEffect

class ExplosionManager:
    def __init__(self):
        self.explosions = pygame.sprite.Group()

    def create_explosion(self, position, frame_speed):
        self.explosions.add(ExplosionEffect(position, frame_speed))

    def update(self, dt):
        self.explosions.update(dt)

    def draw(self, surface):
        self.explosions.draw(surface)

    def __len__(self):
        return len(self.explosions)