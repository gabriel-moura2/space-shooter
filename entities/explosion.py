from pygame import Surface, SRCALPHA
from base.entity import Entity
from utils.helpers import load_image, load_sound

class ExplosionEffect(Entity):
    def __init__(self, position, frame_speed):
        self.spritesheet = load_image("explosion")
        super().__init__(Surface((36, 36), SRCALPHA))
        self.rect.center = position
        self.frame = 0
        self.frame_speed = frame_speed
        load_sound("hit").play()

    def update(self, dt):
        self.frame += self.frame_speed * dt
        if self.frame > 6:
            self.kill()
            return
        
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.spritesheet, (0, 0), (int(self.frame) * 36, 0, 36, 36))
    