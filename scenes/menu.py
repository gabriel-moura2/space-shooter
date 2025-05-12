import pygame
from entities.text import Text
from config import MENU_BACKGROUND
from config import TITLE_X, TITLE_Y, TITLE_SIZE, TITLE_COLOR, HINT_X, HINT_Y, HINT_SIZE, HINT_COLOR


class MenuScene:
    def __init__(self, manager):
        self.manager = manager
        self.texts = [
            Text((TITLE_X,TITLE_Y), "Space Shooter", TITLE_SIZE, TITLE_COLOR),
            Text((HINT_X, HINT_Y), "Enter space", HINT_SIZE, HINT_COLOR)
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
    
    def update(self):
        pass

    def draw(self, screen):
        screen.fill(MENU_BACKGROUND)
        for text in self.texts:
            text.draw(screen)