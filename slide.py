# Created on July 11 2018
import numpy as np
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class grid():
	def __init__(self,size):
		self.size = size

		self.grid_array = np.arange(size**2)
		self.grid = np.random.permutation(self.grid_array).reshape((size,size))



class play(grid):
	def __init__(self,size):
		grid.__init__(self,size)

		# self.x = x
		# self.y = y
		self.turn_count = 0

		solved = (self.grid)+1
		solved[-1] = 0
		solved = solved.reshape([size,size])


		while not np.array_equal(self.grid,solved):
			print(self.grid)
			self.turn()


	def get_move(self):
		self.position = int(input("turn %d: "%(self.turn_count)))
		#clear()
		self.turn_count += 1
		# return self.position

	def slide(self):
			[x],[y] = np.where(self.grid==self.position)

			row = np.setdiff1d(self.grid[x,:],self.position)
			col = np.setdiff1d(self.grid[:,y],self.position)


			# roll mechanics --- jot down the cases
			if (row==0).sum() == 1: # the blank is in this row
				print('moved row')
				self.grid[x] = np.roll(self.grid[x],1)  # if the blank is at either end of the row --- might need to roll different directions accordingly
			elif (col==0).sum() == 1: # the blank is in this col
				print('moved col')
				self.grid[:,y] = np.roll(self.grid[:,y],1) # if the blank is at either end of the col 
			else:
				print('invalid move')

	def turn(self):
		position = self.get_move()
		self.slide()

if __name__ == "__main__":
	n = 4
	play(n)

