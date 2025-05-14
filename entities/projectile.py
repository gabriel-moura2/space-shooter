from entities.entity import Entity
from utils.helpers import load_image
from config import PROJECTILE_SPEED, PROJECTILE_DAMAGE

class Projectile(Entity):
    def __init__(self, position, direction):
        super().__init__(load_image("bullet"))
        self.direction = direction
        if direction == -1:
            self.rect.right = position[0]
        else:
            self.rect.left = position[0]
        self.rect.centery = position[1]
        self.damage = PROJECTILE_DAMAGE
    
    def update(self, dt):
        self.rect = self.rect.move(self.direction * PROJECTILE_SPEED * dt, 0)

