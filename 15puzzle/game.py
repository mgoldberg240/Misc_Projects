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

			def zero_position(self):
				[zx],[zy] = np.where(self.grid==0)
				return zx,zy

			row = np.setdiff1d(self.grid[x,:],self.position)
			col = np.setdiff1d(self.grid[:,y],self.position)

			zx,zy = zero_position(self)

			# roll mechanics --- jot down the cases
			if (row==0).sum() == 1: # the blank is in this row
				print('moved row')
				# print(x,zx)
				dist = abs(y-zy)
				print("distance from %d to zero = %d"%(self.position,dist))
				print("x,y = ",x,y)
				
				count = 0
				while not np.array_equal([zx,zy],[x,y]):# and count < 3:

					self.grid[x,y:zy+1] = np.roll(self.grid[x,y:zy+1],1) # roll part of row
					zx,zy = zero_position(self)
					print("zx,zy = ",zx,zy)
					count += 1
			elif (col==0).sum() == 1: # the blank is in this col
				print('moved col')
				dist = abs(x-zx)
				print("distance from %d to zero = %d"%(self.position,dist))
				# self.grid[:,y] = np.roll(self.grid[:,y],1) # if the blank is at either end of the col 
			else:
				print('invalid move')

	def turn(self):
		position = self.get_move()
		self.slide()

if __name__ == "__main__":
	n = 4
	play(n)

