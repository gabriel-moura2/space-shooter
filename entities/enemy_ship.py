from pygame import PixelArray
from entities.space_ship import SpaceShip
from entities.projectile import Projectile
from utils.helpers import load_image
from config import H_POSITION_ENEMY, SHIP_SPEED, SCREEN_HEIGHT, PROJECTILE_DELAY

class EnemyShip(SpaceShip):
    def __init__(self, position, type, projectile_manager):
        super().__init__(load_image("enemy"), (H_POSITION_ENEMY, position), projectile_manager)
        self.speed = SHIP_SPEED
        type_bit = f'{type:06b}'
        pxarray = PixelArray(self.surface)
        color1 = int(type_bit[-6:-4], 2) * 85, int(type_bit[-4:-2], 2) * 85, int(type_bit[-2:], 2) * 85
        print(color1)
        color2 = 255 - color1[0], 255 - color1[1], 255 - color1[2]
        pxarray.replace((51, 51, 0), color1)
        pxarray.replace((51, 153, 0), color2)
        pxarray.close()

    def shoot(self):
         if self.cooldown <= 0:
            self.projectile_manager.append(Projectile((self.rect.left, self.rect.centery), -1))
            self.cooldown = PROJECTILE_DELAY

    def update(self, dt):
        super().update(dt)
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
                self.speed = -self.speed
    
    def draw(self, screen):
          super().draw(screen)
        