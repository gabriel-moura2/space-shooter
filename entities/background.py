import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Background:
    def __init__(self):
        self.img = pygame.image.load("assets/sprites/space.png").convert()
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()
        self.background = pygame.Surface((SCREEN_WIDTH + self.img_width, SCREEN_HEIGHT + self.img_height))
        for y in range(0, self.background.get_height(), self.img_height):
            for x in range(0, self.background.get_width(), self.img_width):
                self.background.blit(self.img, (x, y))
        self.scroll_speed = 0
        self.scroll_x = 0

    def update(self, dt):
       self.scroll_x = (self.scroll_x + self.scroll_speed * dt) % self.img_width

    def move(self, scroll_speed):
        self.scroll_speed = scroll_speed

    def stop(self):
        self.scroll_speed = 0
    
    def draw(self, screen):
        screen.blit(self.background, (-self.scroll_x, 0))