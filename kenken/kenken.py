# Created by Matthew Goldberg on June 11 2018 (Happy Birthday Alex!)
# Solve a kenken puzzle using backtracking

import numpy as np

def solve(puzzle,minis,operators,targets):
	def game_summary():
		print('puzzle')
		print(puzzle)
		print('minis')
		print(minis)
		print('operators')
		print(op)
		print('target values')
		print(targets) # used for testing
	def advance(x,y):
		if y == n-1: # row position n-1 (end) in col y, advance down a row
			y = 0
			x = x + 1
		else:
			y = y + 1
		flow = 0 # proceeding
		return x,y,flow
	def retreat(x,y):
		if y == 0: # row position 0 in col y, retreat up a row
			y = n - 1
			x = x - 1
			if x < 0:
				x = 0
		else:
			y = y - 1
		flow = 1 # used by given check/mini of size 1 check. 1 means retreating/flowing back
		return x,y,flow
	def available(x,y):
		row_av = np.setdiff1d(allvals,puzzle[x,:])
		col_av = np.setdiff1d(allvals,puzzle[:,y])
		return np.intersect1d(row_av,col_av)
	def full_mini(x,y): # returns 1 if mini is full, 0 otherwise
		if (minis == minis[x,y]).sum() == np.count_nonzero(puzzle*(minis == minis[x,y])): # this is what it means for a mini to be full!
			return 1
		else:
			return 0
	def mini_check(this_mini,op,target):
		current = puzzle[np.equal(minis,this_mini)] # the mini in question, this_mini
		current.sort()
		if op in ['/']:
			mini_val = current[1]/current[0]
		elif op in ['-']:
			mini_val = current[1]-current[0]
		elif op in ['+']:
			mini_val = sum(current)
		elif op in ['*']:
			mini_val = np.prod(current)
		elif op in ['']:
			mini_val = target
		if mini_val == target:
			# print('mini ',this_mini,' is correct')
			return 1
		else:
			# print('mini ',this_mini,' is INCORRECT')
			return 0
	def newturn():
		print('~~~~~~~~~~~~~')
		print('move ',moves)
		print('position [',x,',',y,']...')
		print(puzzle)
	def win():
		print('*****************************')
		print('puzzle completed in %d moves'%(moves))
		print(puzzle)
		# print('number of moves = ',moves)
		print('*****************************')

	allvals = np.array(range(1,n+1)) # e.g. [1,2,3,4] for n = 4 puzzle
	x = 0
	y = 0
	moves  = 0
	flow = 0 # proceeding forwards
	while x <= n-1 and y <= n-1 and moves < 500:
		newturn()
		if (minis == minis[x,y]).sum() == 1: # mini of size 1 is a given
			if flow:
				x,y,_ = retreat(x,y) # move to next
				flow = 0 # proceeding forwards
			else:
				x,y,flow = advance(x,y)
		validval = available(x,y)
		if validval.size == 0: # no legal move at x,y
			puzzle[x,y] = 0
			x,y,flow = retreat(x,y)
		else:
			if puzzle[x,y]==0:
				puzzle[x,y] = np.min(validval,puzzle[x,y])

				if full_mini(x,y): # current mini is full, proceed to mini check
					mini_index = minis[x,y]
					if not mini_check(mini_index,op[mini_index],targets[mini_index]):
						puzzle[x,y] = 0
						x,y,flow = retreat(x,y)
					else:
						x,y,flow = advance(x,y)
				else:
					x,y,flow = advance(x,y)


				# x,y = advance(x,y)
			else: # there is a nonzero value at x,y
				newvalid = np.setdiff1d(validval,puzzle[x,y])
				newvalid = newvalid[newvalid > puzzle[x,y]]
				if newvalid.size == 0: # there are still no legal moves 
					puzzle[x,y] = 0
					x,y,flow = retreat(x,y)
				else:
					newvalid = np.min(newvalid[newvalid > puzzle[x,y]])
					puzzle[x,y] = newvalid
					# print('move ',moves,': im here')
					if full_mini(x,y): # current mini is full, proceed to mini check
						mini_index = minis[x,y]
						if mini_check(mini_index,op[mini_index],targets[mini_index]):
							print('mini %d is correct'%(mini_index))
							x,y,flow = advance(x,y)
						else: 
							print('mini %d is INCORRECT'%(mini_index))
					else:
						x,y,flow = advance(x,y)
		moves = moves + 1
	win()


### SAMPLE PUZZLE 1
# n = 4
# puzzle = np.zeros([n,n])
# puzzle[1,0] = 4
# puzzle = puzzle.astype(int)

# minis = [0,0,1,1,2,3,3,1,4,3,3,5,4,6,6,5]
# minis = np.array(minis)
# minis = np.reshape(minis,[n,n])
# minis = minis.astype(int)

# op = ['/','+','','*','-','/','+']

# targets = [2,7,4,12,2,2,5]

# solve(puzzle,minis,op,targets)





# ### SAMPLE PUZZLE 2
n = 6
puzzle = np.zeros([n,n])
puzzle = puzzle.astype(int)

minis = [0,1,1,2,3,3,0,4,4,2,5,3,6,6,7,7,5,3,6,6,8,9,10,10,11,11,8,9,9,12,13,13,13,14,14,12]
minis = np.array(minis)
minis = np.reshape(minis,[n,n])
minis = minis.astype(int)

op = ['+','/','*','*','-','/','*','*','*','+','*','*','+','+','/']

targets = [11,2,20,6,3,3,240,6,6,7,30,6,9,8,2]

solve(puzzle,minis,op,targets)






