from entities.entity import Entity
from config import HEALTH

class SpaceShip(Entity):
    def __init__(self, surface, position):
        super().__init__(surface)
        self.rect.move_ip(position)

    def hit(self, damage):
        self.health -= damage

    def update(self, dt):
        self.rect = self.rect.move(0, self.speed * dt)
