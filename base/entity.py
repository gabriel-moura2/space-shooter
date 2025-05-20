from pygame.sprite import Sprite

class Entity(Sprite):
    def __init__(self, image):
        Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()

    def update(self, dt):
        pass
