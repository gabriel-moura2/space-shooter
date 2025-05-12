import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.helpers import load_image
from core.scene_manager import SceneManager

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space shooter")
        pygame.display.set_icon(load_image("player"))
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = SceneManager()
        
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.scene_manager.handle_events()
            self.scene_manager.update()
            self.scene_manager.draw(self.screen)
            pygame.display.flip()

