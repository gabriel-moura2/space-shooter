import pygame

class Entity:
    def __init__(self, surface, position):
        self.surface = surface
        self.position = position

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.surface, self.position)
