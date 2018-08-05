import pygame
import random
from classes.map import Map

#Screen/Game Parameters
WIDTH = 500
HEIGHT = 500
FPS = 30

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Tower Defense")
gameClock = pygame.time.Clock()
# initialize instances of assets
gameMap = Map()


# game loop
running = True
while running: 
	# Process input (events)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# Update


	# Draw / render
	gameMap.drawMap(screen)
  
	# after drawing everything, flip the display
	pygame.display.flip()


##### QUIT GAME 
pygame.quit()