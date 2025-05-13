from scenes.scene import Scene
from entities.background import Background
from entities.enemy_ship import EnemyShip
from config import SCREEN_HEIGHT

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self.enemy = EnemyShip(SCREEN_HEIGHT / 2)
        self.entities = [
            Background(),
            self.enemy
        ]

    def handle_events(self):
        super().handle_events()
    
    def update(self, dt):
        super().update(dt)

        if self.enemy.rect.top < 0 or self.enemy.rect.bottom > SCREEN_HEIGHT:
            self.enemy.speed = -self.enemy.speed
    
    def draw(self, screen):
        super().draw(screen)