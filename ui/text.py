from pygame.font import Font
from pygame.sprite import Sprite

class Text(Sprite):
	def __init__(self, position, text, size, color):
		self.font = Font('assets/fonts/ElecstromRegular.ttf', size)
		self.color = color
		Sprite.__init__(self)
		self.image = self.font.render(text, True, color)
		self.rect = self.image.get_rect()
		self.rect.center = position

	def text(self, text):
		self.image = self.font.render(text, True, self.color)
