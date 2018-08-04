import pygame
import random

WIDTH = 500
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# game loop
running = True
while running: 
	# Process input (events)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# Update
	# Draw / render
	screen.fill(BLACK)
	# after drawing everything, flip the display
	pygame.display.flip()







pygame.quit()