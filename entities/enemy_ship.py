from entities.space_ship import SpaceShip
from utils.helpers import load_image
from config import H_POSITION_ENEMY, SHIP_SPEED, SCREEN_HEIGHT, PROJECTILE_DELAY

class EnemyShip(SpaceShip):
    def __init__(self, position, projectile_manager):
        super().__init__(load_image("enemy"), position, projectile_manager)
        self.cooldown = 0

    def shoot(self):
         if self.cooldown <= 0:
            if self.is_double_shot:
                self.projectile_manager.create_projectile((self.rect.left, self.rect.top), -1, self.projectile_config['damage'], self.projectile_config['speed'])
                self.projectile_manager.create_projectile((self.rect.left, self.rect.bottom), -1, self.projectile_config['damage'], self.projectile_config['speed'])
            else:
                self.projectile_manager.create_projectile((self.rect.left, self.rect.centery), -1, self.projectile_config['damage'], self.projectile_config['speed'])
            self.cooldown = PROJECTILE_DELAY

    def update(self, dt):
        if self.rect.x > H_POSITION_ENEMY:
            self.rect = self.rect.move(-SHIP_SPEED * dt, 0)
            return
        super().update(dt)
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed = -self.speed
        if self.cooldown > 0:
            self.cooldown -= dt
        