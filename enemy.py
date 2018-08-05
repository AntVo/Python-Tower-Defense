import pygame

class Enemy: 
	def __init__(self, waypoints):
		self.health = 50,
		self.coordinates = waypoints[0],
		self.waypoints = waypoints,
		self.size = 50,
		self.direction = None,
		self.color = (0,0,0)


	def initiate(self, screen):
		# circle( Surface, color, pos, radius, width)
		pygame.draw.circle(screen, self.color, self.coordinates, 25, 1)


  def render():
  	pygame.draw.circle()