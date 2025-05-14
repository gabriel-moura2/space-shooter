from pygame import Surface
from entities.entity import Entity
from utils.helpers import load_image

class ExplosionEffect(Entity):
    def __init__(self, position):
        self.spritesheet = load_image("explosion")
        super().__init__(Surface.subsurface(self.spritesheet, (0, 0, 36, 36)))
        self.rect.center = position
        self.frame = 0

    def update(self, dt):
        self.frame += 1
        if self.frame > 5:
            self.kill()
            return
        self.image.blit(self.spritesheet, (0, 0), (int(self.frame) * 36, 0, 36, 36))
    