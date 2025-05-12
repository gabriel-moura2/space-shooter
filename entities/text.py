from pygame.font import Font

class Text:
	def __init__(self, position, text, size, color):
		self.font = Font('assets/fonts/ElecstromRegular.ttf', size)
		self.color = color
		self.text = self.font.render(text, True, color)
		self.rect = self.text.get_rect()
		self.rect.center = position

	def update(self):
		pass
	
	def draw(self, screen):
		screen.blit(self.text, self.rect)
