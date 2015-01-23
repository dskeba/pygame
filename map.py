
import pygame
import pytmx
import pyscroll
import math

class map():
	
	def __init__(self, filename, screen):
		self.tmx_data = pytmx.load_pygame(filename)
		self.load_walls(self.tmx_data)
		map_data = pyscroll.data.TiledMapData(self.tmx_data)
		self.map_layer = pyscroll.BufferedRenderer(map_data, screen.get_size())
		self.screen = screen
		self.screen_x = 0
		self.screen_y = 0
		self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer,default_layer=2)
		
	def load_walls(self, tmx_data):
		self.walls = list()
		for object in tmx_data.objects:
			self.walls.append(pygame.Rect(object.x, object.y, object.width, object.height))
	
	def add_sprite(self, sprite):
		self.group.add(sprite)
		
	def update(self):
		self.group.update(0)
		for sprite in self.group.sprites():
			for wall in self.walls:
				if wall.collidepoint(sprite.rect.center):
					sprite.move_back()

	def draw(self, surface, center = None):
		if center:
			self.group.center(center)
		self.group.draw(surface)