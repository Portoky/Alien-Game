import pygame	#module containing the functionality needed to make a game
from pygame.sprite import Group
from setting import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():
	#Initialize pygame, settings, and screen object.
	
	pygame.init()	#initializes the background settings that pygame needs to work properly
	
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))	#we need a tuple here, creates a 
	#^object -> called surface																#display window
	
	pygame.display.set_caption("Alien Invasion")
	
	#Make the Play button.
	play_button = Button(ai_settings, screen, "Play")
	
	#Create an instance to store game statistics.
	stats = GameStats(ai_settings)
	
	#Make a ship, a group of bullets, and a group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	#Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship, 
		aliens,	bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

		
run_game()
	
	
