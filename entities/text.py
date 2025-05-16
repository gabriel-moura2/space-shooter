from pygame.font import Font
from entities.entity import Entity

class Text(Entity):
	def __init__(self, position, text, size, color):
		self.font = Font('assets/fonts/ElecstromRegular.ttf', size)
		self.color = color
		super().__init__(self.font.render(text, True, color))
		self.rect.center = position

	def text(self, text):
		self.image = self.font.render(text, True, self.color)
