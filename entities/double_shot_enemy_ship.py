from entities.enemy_ship import EnemyShip
from entities.projectile import Projectile
from config import PROJECTILE_DELAY

class DoubleShotEnemyShip(EnemyShip):
    def __init__(self, position, type):
        super().__init__(position, type)
    
    def shoot(self, projectiles):
        if self.cooldown <= 0:
            projectiles.add(Projectile((self.rect.left, self.rect.top), -1, self.projectile_config['damage'], self.projectile_config['speed']))
            projectiles.add(Projectile((self.rect.left, self.rect.bottom), -1, self.projectile_config['damage'], self.projectile_config['speed']))
            self.cooldown = PROJECTILE_DELAY
    
    def update(self, dt):
        super().update(dt)