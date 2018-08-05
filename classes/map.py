# Tilemap Parameters
import pygame

class Map:
	def __init__(self):
		grass = (85, 125, 70)
		dirt = (153, 76, 10)
		self.grass = grass
		self.dirt= dirt
		self.mapWidth = 10
		self.mapHeight = 10
		self.tileSize= 50

		self.tileMap = [
			 					[grass, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
			 					[grass, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
			 					[grass, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, grass],
			 					[grass, grass, grass, grass, grass, grass, grass, grass, dirt, grass],
			 					[grass, grass, grass, grass, grass, grass, grass, grass, dirt, grass],
			 					[grass, grass, grass, grass, grass, grass, grass, grass, dirt, grass],
			 					[grass, dirt, dirt, dirt, dirt, dirt, dirt, dirt, dirt, grass],
			 					[grass, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
			 					[grass, dirt, grass, grass, grass, grass, grass, grass, grass, grass],
			 					[grass, dirt, grass, grass, grass, grass, grass, grass, grass, grass]
			 				]

	def drawMap(self, screen):
		for row in range(self.mapWidth):
			for col in range(self.mapHeight):
				pygame.draw.rect(screen, self.tileMap[row][col], (row*self.tileSize,col*self.tileSize, self.tileSize, self.tileSize))	
