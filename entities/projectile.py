from entities.entity import Entity
from utils.helpers import load_image
from config import PROJECTILE_SPEED

class Projectile(Entity):
    def __init__(self, position, direction):
        super().__init__(load_image("bullet"), position)
        self.direction = direction
    
    def update(self, dt):
        self.rect = self.rect.move(self.direction * PROJECTILE_SPEED * dt, 0)

    def draw(self, screen):
        super().draw(screen)

