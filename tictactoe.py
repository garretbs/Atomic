import pygame
from pygame.locals import *

class TicTacToe_Grid():
	def __init__(self):
		self.grid = [
		[' ', ' ', ' '],
		[' ', ' ', ' '],
		[' ', ' ', ' ']
		]
		self.sprite = pygame.sprite.Sprite()
		self.player_symbol = 'X'
		self.cpu_symbol = 'O'
		self.player_color = (0, 0, 191)
		self.cpu_color = (191, 0, 0)
		self.difficulty = 1
		#blit grid lines onto own sprite 
	
	def check_if_solved(self):
		#check horizontals
		for y in range(0, 3):
			if self.grid[0][y] == self.grid[1][y] == self.grid[2][y]:
				if self.grid[0][y] != ' ':
					return (None, y)
		#check verticals
		for x in range(0, 3):
			if self.grid[x][0] == self.grid[x][1] == self.grid[x][2]:
				if self.grid[x][0] != ' ':
					return (x, None)
		#check diagonals
		if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
			if self.grid[0][0] != ' ':
				return ((0,0), (2, 2))
		if self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
			if self.grid[0][2] != ' ':
				return ((0,2), (2, 0))
		return False #return whether player, cpu, or nobody won
	
	def cpu_make_move(self):
		if self.difficulty == 0: #easy
			for y in range(0, 3):
				for x in range(0, 3):
					if self.grid[x][y] == ' ':
						self.grid[x][y] = self.cpu_symbol
						return [x, y]
		elif self.difficulty == 1: #medium
			if self.grid[1][1] == ' ': #try for center
				self.grid[1][1] = self.cpu_symbol
				return [1, 1]
			elif self.grid[0][0] == ' ': #try for corners
				self.grid[0][0] = self.cpu_symbol
				return [0, 0]
			elif self.grid[0][2] == ' ': 
				self.grid[0][2] = self.cpu_symbol
				return [0, 2]
			elif self.grid[2][0] == ' ': 
				self.grid[2][0] = self.cpu_symbol
				return [2, 0]
			elif self.grid[2][2] == ' ': 
				self.grid[2][2] = self.cpu_symbol
				return [2, 2]
			elif self.grid[1][0] == ' ': #try the rest
				self.grid[1][0] = self.cpu_symbol
				return [1, 0]
			elif self.grid[0][1] == ' ':
				self.grid[0][1] = self.cpu_symbol
				return [0, 1]
			elif self.grid[2][1] == ' ':
				self.grid[2][1] = self.cpu_symbol
				return [2, 1]
			elif self.grid[1][2] == ' ':
				self.grid[1][2] = self.cpu_symbol
				return [1, 2]
		else: #impossible
			pass
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
	pygame.display.set_caption("Tic Tac Toe")
	bg = pygame.Surface(size)
	bg = bg = bg.convert()
	bg.fill((63, 63, 63))
	
	#Text Stuff
	fcolor = (191, 191, 191)
	font = pygame.font.Font(None, int(size[1]/15))
	text = font.render("Tic Tac Toe!", 1, fcolor)
	pos = text.get_rect()
	pos.centerx = bg.get_rect().centerx
	pos.centery = bg.get_rect().centery
	bg.blit(text, pos)
	font = pygame.font.Font(None, size[1]>>1)
	
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
	grid = TicTacToe_Grid()
	
	while True:
		for event in pygame.event.get():
				if event.type == QUIT:
						return
				elif event.type == MOUSEBUTTONDOWN:
					#get click position, pass into grid to determine stuff
					#then cpu makes move after waiting x frames
					#skip if click is directly on or outside grid
					pos = grid.player_make_move(event.pos[0]/size[0], event.pos[1]/size[1])
					if pos is None:
						break
					text = font.render(grid.player_symbol, 1, grid.player_color)
					pos[0] = pos[0] * size[0]/3 + size[0]/12
					pos[1] = pos[1] * size[1]/3
					bg.blit(text, pos)
					
					screen.blit(bg, (0,0))
					#blit this stuff to the bg instead
					pygame.draw.line(screen, fcolor, line1[0], line1[1], ls)
					pygame.draw.line(screen, fcolor, line2[0], line2[1], ls)
					pygame.draw.line(screen, fcolor, line3[0], line3[1], ls)
					pygame.draw.line(screen, fcolor, line4[0], line4[1], ls)
					pygame.display.update()
					
					if grid.check_if_solved():
						pygame.time.delay(250)
						#pygame.draw.line(screen, fcolor, line1[0], line1[1], ls)
						#draw line striking through, flash screen
						print("Player won!")
						pygame.time.delay(1500)
						return
					
					pygame.time.delay(500)
					pos = grid.cpu_make_move()
					if pos is None:
						print("Tie")
						pygame.time.delay(1500)
						return
					text = font.render(grid.cpu_symbol, 1, grid.cpu_color)
					pos[0] = pos[0] * size[0]/3 + size[0]/12
					pos[1] = pos[1] * size[1]/3
					bg.blit(text, pos)
					screen.blit(bg, (0,0))
					#blit this stuff to the bg instead
					pygame.draw.line(screen, fcolor, line1[0], line1[1], ls)
					pygame.draw.line(screen, fcolor, line2[0], line2[1], ls)
					pygame.draw.line(screen, fcolor, line3[0], line3[1], ls)
					pygame.draw.line(screen, fcolor, line4[0], line4[1], ls)
					pygame.display.update()
					if grid.check_if_solved():
						#pygame.draw.line(screen, fcolor, line1[0], line1[1], ls)
						#draw line striking through, flash screen
						print("CPU won!")
						pygame.time.delay(1500)
						return
					pygame.event.clear()
				#pygame.display.flip()
		screen.blit(bg, (0,0))
		#blit this stuff to the bg instead
		pygame.draw.line(screen, fcolor, line1[0], line1[1], ls)
		pygame.draw.line(screen, fcolor, line2[0], line2[1], ls)
		pygame.draw.line(screen, fcolor, line3[0], line3[1], ls)
		pygame.draw.line(screen, fcolor, line4[0], line4[1], ls)
		pygame.display.flip()

if __name__ == '__main__': main()