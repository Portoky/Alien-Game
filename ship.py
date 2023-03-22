import pygame

class Ship():
	
	def __init__(self, ai_settings, screen):
		'''Initialze the ship and its starting position.'''
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Start each new ship at the bottom of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Store a decimal value for the ship's center.
		self.centerx = float(self.rect.centerx)  #otherwise rect would only store an integer
												#more punctual later
		#Movement flags
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		'''Update the ship's position based on the movement flags.'''
		#Update the ship's center value not the rect.
		
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:	# <==> 0
			self.centerx -= self.ai_settings.ship_speed_factor
			
		#Update rect object from self.center.
		self.rect.centerx = self.centerx	#only integer but its ok :)
	
	def blitme(self):
		'''Deaw the ship at its current location.'''
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		'''Center the ship on the screen.'''
		self.rect.centerx = self.screen_rect.centerx
	
