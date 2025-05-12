import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        
    def run(self):
        while self.running:
            pygame.display.flip()
            self.clock.tick(FPS)
