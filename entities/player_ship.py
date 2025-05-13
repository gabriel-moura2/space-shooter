from entities.space_ship import SpaceShip
from entities.projectile import Projectile
from utils.helpers import load_image
from config import H_POSITION_PLAYER, SCREEN_HEIGHT, PROJECTILE_DELAY

class PlayerShip(SpaceShip):
    def __init__(self, projectile_manager):
        super().__init__(load_image("player"), (H_POSITION_PLAYER, SCREEN_HEIGHT / 2), projectile_manager)

    def update(self, dt):
        if self.rect.top + self.speed * dt < 0 or self.rect.bottom + self.speed * dt > SCREEN_HEIGHT:
             return
        super().update(dt)

    def shoot(self):
         if self.cooldown <= 0:
            self.projectile_manager.append(Projectile((self.rect.right, self.rect.centery), 1))
            self.cooldown = PROJECTILE_DELAY
    
    def draw(self, screen):
          super().draw(screen)