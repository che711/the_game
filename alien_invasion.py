import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_function as gf 

# python3 alien_invasion.py

def run_game():
	#Иницилизирует pygame, settings и объекты экрана
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_height,ai_settings.screen_width))
	pygame.display.set_caption("Alien Invasion")
	
	#Создание кнопки Play
	play_button=Button(ai_settings,screen, "Play")
	
	#Создание экземпляр GameStats и Scoreboard.
	stats=GameStats(ai_settings) 
	sb=Scoreboard(ai_settings,screen,stats)
	
	#Создание корабля, группы хрранения пуль и пришельцев
	ship=Ship(ai_settings, screen)
	bullets=Group()
	aliens=Group()
	 
	#Создание флота пришельцев
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Запуск основного цикла игры
	while True:
		#Отслеживание событий клавиатуры и мыши.
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()		
				
