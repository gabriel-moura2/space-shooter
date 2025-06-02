import pygame
import math
from base.entity import Entity
from utils.helpers import load_image
from utils.helpers import load_sound
from config import SCREEN_WIDTH

class Projectile(Entity):
    def __init__(self, position, angle, damage, speed):
        super().__init__(load_image("bullet"))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.speed_x = math.cos(angle) * speed
        self.speed_y = math.sin(angle) * speed
        if self.speed_x < 0:
            self.rect.right = position[0]
        else:
            self.rect.left = position[0]
        self.rect.centery = position[1]
        self.damage = damage
        load_sound("laser").play()
    
    def update(self, dt):
        self.rect = self.rect.move(self.speed_x * dt, self.speed_y * dt)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.kill()
