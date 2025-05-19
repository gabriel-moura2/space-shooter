import pygame
from scenes.scene import Scene
from entities.text import Text
from config import GAME_OVER_DISPLAY_CONFIG, SCORE_DISPLAY_CONFIG, TO_MENU_DISPLAY_CONFIG

class GameOverScene(Scene):
    def __init__(self, manager, score):
        super().__init__(manager)
        self.sprite_groups = {
            "texts": pygame.sprite.Group(
                Text(**GAME_OVER_DISPLAY_CONFIG),
                Text(**SCORE_DISPLAY_CONFIG, text=f"Score {score}"),
                Text(**TO_MENU_DISPLAY_CONFIG)
            )
        }

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                from scenes.menu import MenuScene
                self.manager.change_scene(MenuScene(self.manager))