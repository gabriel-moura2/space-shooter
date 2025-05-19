import pygame
from scenes.scene import Scene
from entities.text import Text
from config import MENU_BACKGROUND_COLOR
from config import TITLE_DISPLAY_CONFIG, START_DISPLAY_CONFIG


class MenuScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        self.texts = pygame.sprite.Group()
        self.texts.add(Text(**TITLE_DISPLAY_CONFIG))
        self.texts.add(Text(**START_DISPLAY_CONFIG))
        self.entities = [self.texts]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                from scenes.level import LevelScene
                self.manager.change_scene(LevelScene(self.manager, 1))
    
    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        screen.fill(MENU_BACKGROUND_COLOR)
        super().draw(screen)
