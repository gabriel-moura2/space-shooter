from pygame.font import Font
from entities.entity import Entity

class Text(Entity):
	def __init__(self, position, text, size, color):
		self.font = Font('assets/fonts/ElecstromRegular.ttf', size)
		self.color = color
		super().__init__(self.font.render(text, True, color), [0, 0])
		self.rect.center = position

	def update(self, dt):
		super().update(dt)
	
	def draw(self, screen):
		screen.blit(self.surface, self.rect)
