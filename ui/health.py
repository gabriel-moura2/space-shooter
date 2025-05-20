from pygame import Surface, SRCALPHA
from pygame.sprite import Sprite
from utils.helpers import load_image
from config import HEALTH

class HealthDisplay(Sprite):
    def __init__(self, space_ship):
        Sprite.__init__(self)
        self.image = Surface((21, 7), SRCALPHA)
        self.rect = self.image.get_rect()
        self.sprite = load_image("heart")
        self.rect.move_ip(space_ship.rect.left, space_ship.rect.top - 7)
        self.space_ship = space_ship
    
    def update(self, dt):
        self.rect.x = self.space_ship.rect.left
        self.rect.y = self.space_ship.rect.top - 7
        self.image.fill((0, 0, 0, 0))
        for i in range(self.space_ship.health):
            self.image.blit(self.sprite, (i * 7, 0))
    
