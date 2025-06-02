import pygame
from base.scene import Scene
from ui.text import Text
from config import MENU_BACKGROUND_COLOR
from config import TITLE_DISPLAY_CONFIG, START_DISPLAY_CONFIG


class MenuScene(Scene):
    def __init__(self, manager, input_handler):
        super().__init__(manager, input_handler)
        self.sprite_groups = {
            "ui": pygame.sprite.Group(Text(**TITLE_DISPLAY_CONFIG), Text(**START_DISPLAY_CONFIG))
        }

    def handle_input_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            from scenes.level import LevelScene
            self.manager.change_scene(LevelScene(self.manager, self.input_handler, 34))
    
    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        screen.fill(MENU_BACKGROUND_COLOR)
        super().draw(screen)
