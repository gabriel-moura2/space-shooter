import pygame
from scenes.scene import Scene
from entities.text import Text
from config import GAME_OVER_X, GAME_OVER_Y, GAME_OVER_SIZE, GAME_OVER_COLOR, SCORE_X, SCORE_Y, SCORE_SIZE, SCORE_COLOR, HINT_X, HINT_Y, HINT_COLOR, HINT_SIZE

class GameOverScene(Scene):
    def __init__(self, manager, score):
        super().__init__(manager)
        self.texts = pygame.sprite.Group()
        self.texts.add(Text((GAME_OVER_X, GAME_OVER_Y), "Game Over", GAME_OVER_SIZE, GAME_OVER_COLOR))
        self.texts.add(Text((SCORE_X, SCORE_Y), f"Score {score}", SCORE_SIZE, SCORE_COLOR))
        self.texts.add(Text((HINT_X, HINT_Y), "press P to menu", HINT_SIZE, HINT_COLOR))
        self.entities = [self.texts]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                from scenes.menu import MenuScene
                self.manager.change_scene(MenuScene(self.manager))