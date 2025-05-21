import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.helpers import load_image
from core.scene_manager import SceneManager
from system.input_handler import InputHandler

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space shooter")
        pygame.display.set_icon(load_image("player"))
        self.clock = pygame.time.Clock()
        self.running = True
        self.input_handler = InputHandler()
        self.scene_manager = SceneManager(self.input_handler)
        
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            self.input_handler.handle_events()
            self.input_handler.handle_pressed_keys()
            self.scene_manager.update(dt)
            self.scene_manager.draw(self.screen)
            pygame.display.flip()

