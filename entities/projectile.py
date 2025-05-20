from base.entity import Entity
from utils.helpers import load_image
from utils.helpers import load_sound
from config import SCREEN_WIDTH

class Projectile(Entity):
    def __init__(self, position, direction, damage, speed):
        super().__init__(load_image("bullet"))
        self.direction = direction
        if direction == -1:
            self.rect.right = position[0]
        else:
            self.rect.left = position[0]
        self.rect.centery = position[1]
        self.damage = damage
        self.speed = speed
        load_sound("laser").play()
    
    def update(self, dt):
        self.rect = self.rect.move(self.direction * self.speed * dt, 0)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.kill()
