from pygame import Rect
from entities.entity import Entity
from utils.helpers import load_image

class ExplosionEffect(Entity):
    def __init__(self, position):
        super().__init__(load_image("explosion"), position)
        self.frame = Rect(0, 0, self.rect.height, self.rect.height)

    def update(self, dt):
        self.frame.left += self.rect.height
        if self.frame.right > self.rect.height * 6:
            self.frame.left = 0
    