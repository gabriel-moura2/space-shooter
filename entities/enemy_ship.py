from pygame import PixelArray
import colorsys
from entities.space_ship import SpaceShip
from entities.projectile import Projectile
from utils.helpers import load_image
from config import H_POSITION_ENEMY, SHIP_SPEED, SCREEN_HEIGHT, PROJECTILE_DELAY

class EnemyShip(SpaceShip):
    def __init__(self, position, type):
        super().__init__(load_image("enemy"), (H_POSITION_ENEMY, position))
        self.speed = SHIP_SPEED
        self.cooldown = 0
        type_bit = f'{type:06b}'
        pxarray = PixelArray(self.image)
        color1 = int(type_bit[-6:-4], 2) * 85, int(type_bit[-4:-2], 2) * 85, int(type_bit[-2:], 2) * 85
        hsv = colorsys.rgb_to_hsv(color1[0] / 255, color1[1] / 255, color1[2] / 255)
        rgb = colorsys.hsv_to_rgb((hsv[0] - (1/9)) % 1, hsv[1], hsv[2] / 3)
        color2 = int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        pxarray.replace((51, 51, 0), color2)
        pxarray.replace((51, 153, 0), color1)
        pxarray.close()

    def shoot(self, projectiles):
         if self.cooldown <= 0:
            projectiles.add(Projectile((self.rect.left, self.rect.centery), -1))
            self.cooldown = PROJECTILE_DELAY

    def update(self, dt):
        super().update(dt)
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed = -self.speed
        if self.cooldown > 0: 
            self.cooldown -= dt
        