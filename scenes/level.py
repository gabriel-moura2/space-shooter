import pygame
from scenes.scene import Scene
from entities.background import Background
from utils.helpers import load_image

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self.background = Background()

    def handle_events(self):
        super().handle_events()
    
    def update(self):
        super().update()
    
    def draw(self, screen):
        self.background.draw(screen)
        super().draw(screen)