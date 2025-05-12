import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Background:
    def __init__(self):
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img = pygame.image.load("assets/sprites/space.png").convert()
        tile_width = self.img.get_width()
        tile_height = self.img.get_height()
        for y in range(0, SCREEN_HEIGHT, tile_height):
            for x in range(0, SCREEN_WIDTH, tile_width):
                self.background.blit(self.img, (x, y))
    
    def draw(self, screen):
        screen.blit(self.background, (0, 0))