import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''A class to manage bullets fired from the ship.'''
	
	def __init__(self, ai_settings, screen, ship):
		'''Create a bullet object at the ship's current position.'''
		super(Bullet, self).__init__()
		self.screen = screen
	
		# Create a bullet rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)	#not based on an image -> we make it from scratch
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top	# we adjust to the correct location->
		#bullet emerges from the top of the ship //->dependent on the ships position
		
		#store the bullet's position as a decimal value, fine adjustments
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		'''Move the bullet up the screen.'''
		#Update the decimal position of the bullet.
		self.y -= self.speed_factor
		#Update the rect position
		self.rect.y = self.y
		
	def draw_bullet(self):
		'''Draw the bullet to the screen.'''
		pygame.draw.rect(self.screen, self.color, self.rect)
