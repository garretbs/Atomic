import pygame
from pygame.locals import *

class ConnectFour_Grid():
	def __init__(self):
		self.grid = [
		[' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ', ' '],
		]
		self.player_symbol = 'B'
		self.cpu_symbol = 'R'
		self.player_color = (0, 0, 191)
		self.cpu_color = (191, 0, 0)
	
	def check_if_solved(self):
		#check horizontals
		return False #return whether player, cpu, or nobody won
	
	def cpu_make_move(self):
		return None
	
	def player_make_move(self, x, y):
		#replace this with 9 rect objects, check if xy is inside any of them
		if x < 0.33333:
			x = 0
		elif x < 0.66667:
			x = 1
		else:
			x = 2
		if y < 0.33333:
			y = 0
		elif y < 0.66667:
			y = 1
		else:
			y = 2
		if self.grid[x][y] == ' ':
			self.grid[x][y] = self.player_symbol
		else:
			print("Spot's already taken!")
			return None
		#print(x, y)
		return [x, y]


def main():
	#Prep and initialization
	pygame.init()
	size = 320, 240
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Connect Four")
	bg = pygame.Surface(size)
	bg = bg = bg.convert()
	bg.fill((63, 63, 63))
	
	#Text Stuff
	fcolor = (191, 191, 191)
	
	#Line stuff
	ls = 3
	
	l1x = size[0]/3
	l1y = 16
	l1h = size[1]-l1y
	line1 = ((l1x, l1y),(l1x,l1h))
	
	l2x = size[0]-l1x
	line2 = ((l2x, l1y),(l2x,l1h))
	
	l3x = 16
	l3w = size[0]-l3x
	l3y = size[1]/3
	line3 = ((l3x, l3y),(l3w,l3y))
	
	l4y = size[1]-l3y
	line4 = ((l3x, l4y),(l3w,l4y))
	
	#game variables
	grid = ConnectFour_Grid()
	
	while True:
		for event in pygame.event.get():
				if event.type == QUIT:
						return
				elif event.type == MOUSEBUTTONDOWN:
					pygame.event.clear()
				#pygame.display.flip()
		screen.blit(bg, (0,0))
		pygame.display.flip()

if __name__ == '__main__': main()