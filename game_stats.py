class GameStats():
	"""Отслеживает статистику для игры Alien Invision"""
	def __init__(self,ai_settings):
		"""Инициализирует статистику"""
		self. ai_settings=ai_settings
		self.reset_stats()
		#Игра запускается в неактивном состоянии
		self.game_active=False
		#Игра Alien Invasion запускается в активном состоянии
		self.game_active=True
		#Рекорд не должен сбрасываться
		self.high_score=0
				
	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры"""
		self.ship_left=self.ai_settings.ship_limit	
		self.score=0
		
	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры"""
		self.ship_left=self.ai_settings.ship_limit
		self.score=0
		self.level=1	
