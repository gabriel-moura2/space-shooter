import pygame
from scenes.scene import Scene
from utils.helpers import load_image

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self.background = load_image("space")

    def handle_events(self):
        super().handle_events()
    
    def update(self):
        super().update()
    
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        super().draw(screen)