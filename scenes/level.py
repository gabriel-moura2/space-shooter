from scenes.scene import Scene
from entities.background import Background

class LevelScene(Scene):
    def __init__(self, manager, level):
        super().__init__(manager)
        self.level = level
        self.entities = [
            Background()
        ]

    def handle_events(self):
        super().handle_events()
    
    def update(self, dt):
        super().update(dt)
    
    def draw(self, screen):
        super().draw(screen)