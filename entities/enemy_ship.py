from pygame import PixelArray
import colorsys
from entities.space_ship import SpaceShip
from entities.projectile import Projectile
from utils.helpers import load_image
from config import H_POSITION_ENEMY, SHIP_SPEED, SCREEN_HEIGHT, PROJECTILE_DELAY, PROJECTILE_SPEED, PROJECTILE_DAMAGE, HEALTH

class EnemyShip(SpaceShip):
    def __init__(self, position, type):
        super().__init__(load_image("enemy"), position)
        self.cooldown = 0
        self.projectile_config = {
            'damage': PROJECTILE_DAMAGE * ((type >> 2 & 1) + 1),
            'speed': PROJECTILE_SPEED * ((type >> 1 & 1) + 1)
        }
        self.speed = SHIP_SPEED * ((type >> 3 & 1) + 1)
        self.health = HEALTH * ((type & 1) + 1)
        pxarray = PixelArray(self.image)
        color1 = 255 - (type >> 4) * 85, 255 - (type >> 2 & 3) * 85, 255 - (type & 3) * 85
        hsv = colorsys.rgb_to_hsv(color1[0] / 255, color1[1] / 255, color1[2] / 255)
        rgb = colorsys.hsv_to_rgb((hsv[0] - (1/9)) % 1, hsv[1], hsv[2] / 3)
        color2 = int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        pxarray.replace((51, 51, 0), color2)
        pxarray.replace((51, 153, 0), color1)
        pxarray.close()

    def shoot(self, projectiles):
         if self.cooldown <= 0:
            projectiles.add(Projectile((self.rect.left, self.rect.centery), -1, self.projectile_config['damage'], self.projectile_config['speed']))
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
        