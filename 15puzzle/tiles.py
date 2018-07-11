import numpy as np


class grid():
	def __init__(self,size):
		self.size = size

		grid = np.arange(size**2)
		grid = np.random.permutation(grid).reshape((n,n))
		print(grid)



class play(grid):
	def __init__(self,size):
		grid.__init__(self,size)

		# self.x = x
		# self.y = y
		self.turn = 0

	def get_move(self):
		position = int(input("turn %d"%(turn)))
		self.turn += 1
		return position
	
	def slide(self):
		position = self.get_move()
		def turn():
			[x],[y] = np.where(self.grid==position)
			row = np.setdiff1d(grid[x,:],position)
			col = np.setdiff1d(grid[:,y],position)
			if row.sum() == 1: # the blank is in this row
				print('row')
			elif col.sum() == 1: # the blank is in this col
				print('col')

if __name__ == "__main__":
	n = 4
	play(n)