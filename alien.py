import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Класс, представляющий одного пришельца"""
	
	def __init__(self, ai_settings, screen):
		"""Инициализирует одного пришельца"""
		super (Alien, self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#Загрузка изображения пришельца
		self.image=pygame.image.load('images/alien.bmp')
		self.rect=self.image.get_rect()
		#Задаем координату появления пришельцев в левом верхнем углу
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		#Сохранение точной позиции
		self.x=float(self.rect.x)
	
	def blitme(self):
		"""выводит пришельца в текущем положении"""
		self.screen.blit(self.image, self.rect)	
	
	def check_edges(self):
		"""возвращает True, если пришелец находится у края экрана"""
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True	
							
	def update(self):
		"""перемещает пришельца влево-вправо"""
		self.x+=(self.ai_settings.alien_speed_factor*
			self.ai_settings.fleet_direction)
		self.rect.x=self.x
