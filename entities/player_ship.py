from entities.space_ship import SpaceShip
from entities.projectile import Projectile
from utils.helpers import load_image
from config import H_POSITION_PLAYER, SCREEN_HEIGHT, PROJECTILE_SPEED, PROJECTILE_DAMAGE

class PlayerShip(SpaceShip):
    def __init__(self):
        super().__init__(load_image("player"), (H_POSITION_PLAYER, SCREEN_HEIGHT / 2))

    def update(self, dt):
        if self.rect.top + self.speed * dt < 0 or self.rect.bottom + self.speed * dt > SCREEN_HEIGHT:
             return
        super().update(dt)

    def shoot(self, projectiles):
        projectiles.add(Projectile((self.rect.right, self.rect.centery), 1, PROJECTILE_DAMAGE, PROJECTILE_SPEED))