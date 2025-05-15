from entities.entity import Entity
from entities.explosion import ExplosionEffect
from utils.helpers import load_image

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
    
    def update(self, dt):
        self.rect = self.rect.move(self.direction * self.speed * dt, 0)
    
    def explode(self, explosions):
        explosions.add(ExplosionEffect(self.rect.center, 36))
