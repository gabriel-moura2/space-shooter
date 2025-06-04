import pygame
from base.scene import Scene
from ui.text import Text
from config import CONGRATULATIONS_DISPLAY_CONFIG, TO_MENU_DISPLAY_CONFIG

class CongratulationsScene(Scene):
    def __init__(self, manager, input_handler):
        super().__init__(manager, input_handler)
        self.sprite_groups = {
            "ui": pygame.sprite.Group(
                Text(**CONGRATULATIONS_DISPLAY_CONFIG),
                Text(**TO_MENU_DISPLAY_CONFIG)
            )
        }

    def handle_input_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            from scenes.menu import MenuScene
            self.manager.change_scene(MenuScene(self.manager, self.input_handler))