class Entity:
    def __init__(self, surface, position):
        self.surface = surface
        self.rect = surface.get_rect()
        self.rect.move_ip(position)

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
