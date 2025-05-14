from entities.entity import Entity
from config import HEALTH

class SpaceShip(Entity):
    def __init__(self, surface, position, projectile_manager):
        super().__init__(surface, position)
        self.health = HEALTH
        self.speed = 0
        self.projectile_manager = projectile_manager

    def hit(self, damage):
        self.health -= damage

    def update(self, dt):
        self.rect = self.rect.move(0, self.speed * dt)

    def draw(self, screen):
        super().draw(screen)
