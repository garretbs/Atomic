import random

class ConnectFour_Grid:
	def __init__(self):
		self.player_symbol = 'X'
		self.cpu_symbol = 'O'
		self.slots_taken = 0
		self.grid = []
		self.cols = ['0','1','2','3','4','5','6']
		for i in range(0, 6):
			self.grid.append([' '] * 7)
	
	def print(self):
		print(self.cols)
		for i in range(0, len(self.grid)):
			print(self.grid[i])
	
	def player_place(self, column):
		i = 5
		while True:
			if self.grid[i][column] == ' ':
				self.grid[i][column] = self.player_symbol
				self.slots_taken += 1
				return True
			elif i <= 0:
				return False
			i -= 1
	
	def cpu_place(self):
		attempts = [0,1,2,3,4,5,6]
		random.shuffle(attempts)
		for column in attempts:
			i = 5
			while True:
				if self.grid[i][column] == ' ':
					self.grid[i][column] = self.cpu_symbol
					self.slots_taken += 1
					return True
				elif i <= 0:
					break
				i -= 1
	
	def check_for_winner(self):
		#check rows for horizontal win
		for row in range(0, 6):
			for column in range(0, 4):
				if self.horizontal_equal(row, column) and self.grid[row][column] != ' ':
					return True
		#check columns for vertical win
		for row in range(0, 3):
			for column in range(0, 7):
				if self.vertical_equal(row, column) and self.grid[row][column] != ' ':
					return True
		#painstakingly check for diagonal win
		for row in range(0, 3):
			if self.diagonal_downright_equal(row, 0) and self.grid[row][0] != ' ':
				return True
		return False
	
	def horizontal_equal(self, row, column):
		return self.grid[row][column] == self.grid[row][column+1] and\
		self.grid[row][column] == self.grid[row][column+2] and\
		self.grid[row][column] == self.grid[row][column+3]
	
	def vertical_equal(self, row, column):
		return self.grid[row][column] == self.grid[row+1][column] and\
		self.grid[row][column] == self.grid[row+2][column] and\
		self.grid[row][column] == self.grid[row+3][column]
	
	def diagonal_downright_equal(self, row, column):
		return self.grid[row][column] == self.grid[row+1][column+1] and\
		self.grid[row][column] == self.grid[row+2][column+2] and\
		self.grid[row][column] == self.grid[row+3][column+3]
	
	def diagonal_upright_equal(self, row, column):
		return self.grid[row][column] == self.grid[row-1][column+1] and\
		self.grid[row][column] == self.grid[row-2][column+2] and\
		self.grid[row][column] == self.grid[row-3][column+3]

def main():
	grid = ConnectFour_Grid()
	
	while True:
		grid.print()
		try:
			if grid.slots_taken >= 42:
				print("That's it! No more room")
				return
			col = int(input("Choose your column: "))
			if col > len(grid.grid):
				print("Not a valid position")
			elif not grid.player_place(col):
				print("No more room there! Try again.")
			else:
				if grid.slots_taken >= 42:
					print("That's it! No more room")
					return
				print()
				grid.print()
				input()
				if grid.check_for_winner():
					print("You won! Goodbye")
					return
				#delay, then do cpu move
				grid.cpu_place()
				#check for winner
				if grid.check_for_winner():
					print("CPU won. hah lose")
					return
		except ValueError:
			print("That's not a number")

if __name__ == '__main__': main()