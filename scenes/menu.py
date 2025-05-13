import pygame
from scenes.scene import Scene
from scenes.level import LevelScene
from entities.text import Text
from config import MENU_BACKGROUND_COLOR
from config import TITLE_X, TITLE_Y, TITLE_SIZE, TITLE_COLOR, HINT_X, HINT_Y, HINT_SIZE, HINT_COLOR


class MenuScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                self.manager.change_scene(LevelScene(self.manager, 1))
    
    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        screen.fill(MENU_BACKGROUND_COLOR)
        super().draw(screen)
    
    @property
    def entities(self):
        return [
            Text((TITLE_X,TITLE_Y), "Space Shooter", TITLE_SIZE, TITLE_COLOR),
            Text((HINT_X, HINT_Y), "Enter space", HINT_SIZE, HINT_COLOR)
        ]
