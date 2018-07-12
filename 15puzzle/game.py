# Created by Matt Goldberg on July 11 2018

import numpy as np
import os


def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()

class grid():
	def __init__(self,size):
		self.size = size

		self.grid_array = np.arange(size**2)
		self.rand_array = np.random.permutation(self.grid_array)

		self.grid = self.rand_array.reshape((size,size))
		print(self.grid)



class play(grid):
	def __init__(self,size):
		grid.__init__(self,size)

		# self.x = x
		# self.y = y
		self.turn_count = 0

		# solved state of puzzle
		solved = (self.grid_array)+1
		solved[-1] = 0
		solved = solved.reshape([size,size])

		while not np.array_equal(self.grid,solved): # play until the puzzle is solved
			print(self.grid)
			self.turn()


	def get_move(self):
		print('')
		self.position = int(input("turn %d: "%(self.turn_count)))
		clear()
		self.turn_count += 1
		# return self.position

	def slide(self):
			[x],[y] = np.where(self.grid==self.position)

			def zero_position(self):
				[zx],[zy] = np.where(self.grid==0)
				return zx,zy # zero x and y coordinates

			row = np.setdiff1d(self.grid[x,:],self.position)
			col = np.setdiff1d(self.grid[:,y],self.position)

			zx,zy = zero_position(self)

			# roll mechanics --- jot down the cases
			if (row==0).sum() == 1: # the blank is in this row
				if zy < y: # zero is left of selected tile
					group = np.hstack((self.grid[x,zy+1:y+1],0))
					self.grid[x,zy:y+1] = group
				else: # zero is right of selected tile
					group = np.hstack((0,self.grid[x,y:zy]))
					self.grid[x,y:zy+1] = group



			elif (col==0).sum() == 1: # the blank is in this col
				if zx < x: # zero is below selected tile
					group = np.hstack((self.grid[zx+1:x+1,y],0))
					self.grid[zx:x+1,y] = group
				else: # zero is above of selected tile
					group = np.hstack((0,self.grid[x:zx,y]))
					self.grid[x:zx+1,y] = group
			else:
				print('invalid move')

	def turn(self):
		position = self.get_move()
		self.slide()

if __name__ == "__main__":
	#n = 4
	play(n)

