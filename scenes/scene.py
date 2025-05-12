import pygame

class Scene:
    def __init__(self, manager):
        self.manager = manager
        self.entities = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
    
    def update(self):
        pass

    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen)
