import pygame

class Scene:
    def __init__(self, manager, input_handler):
        self.manager = manager
        self.input_handler = input_handler
        self.input_handler.attach(self)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

    def handle_keys(self, pressed_keys):
        pass
    
    def update(self, dt):
        for group in self.sprite_groups.values():
            group.update(dt)

    def draw(self, screen):
        for group in self.sprite_groups.values():
            group.draw(screen)
