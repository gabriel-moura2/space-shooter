from entities.entity import Entity
from config import HEALTH, SHIP_SPEED

class SpaceShip(Entity):
    def __init__(self, surface, position):
        super().__init__(surface, position)
        self.health = HEALTH
        self.speed = SHIP_SPEED

    def hit(self, damage):
        self.health -= damage

    def update(self, dt):
        self.rect = self.rect.move(0, self.speed * dt)

    def draw(self, screen):
        super().draw(screen)
