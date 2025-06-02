from base.entity import Entity
from entities.explosion import ExplosionEffect
from config import SCREEN_HEIGHT

class SpaceShip(Entity):
    def __init__(self, surface, position, projectile_manager):
        super().__init__(surface)
        self.rect.move_ip(position)
        self.projectile_manager = projectile_manager

    def hit(self, damage):
        self.health -= damage

    def update(self, dt):
        self.rect = self.rect.move(0, self.speed * dt)
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
