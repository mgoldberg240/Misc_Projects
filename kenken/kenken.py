## Created by Matt Goldberg on July 5 2018
# Solve kenken puzzle using backtracking algorithm
#
# parameters:
# -- n ---------------- puzzle side length; integer; e.g. 4
# -- minis ------------ cages, define an arithmetic problem; array; e.g. minis = [0,0,1,1,2,3,3,1,4,3,3,5,4,6,6,5]
# -- operators -------- arithmetic operator symbols; list; e.g. op = ['/','+','!','*','-','/','+']
# -- targets ---------- target mini valuesarray; e.g. targets = [2,7,4,12,2,2,5]

import numpy as np
from timeit import default_timer as timer

def solve(n,puzzle,minis,operators,targets):
	start = timer()

	def game_summary():
		print('puzzle')
		print(puzzle)
		print('minis')
		print(minis)
		print('operators')
		print(op)
		print('target values')
		print(targets) # used for testing

	def newturn():
		print('~~~~~~~~~~~~~')
		print('move ',moves)
		print('position [',x,',',y,']...')
		print(puzzle)

	def win():
		print('*****************************')
		print(puzzle)
		end = timer()
		time = end - start
		print('puzzle completed in %d moves'%(moves))
		print('elapsed time %f seconds'%(time))
		# print('number of moves = ',moves)
		print('*****************************')

	def advance(x,y):
		if y == n-1: # row position n-1 (end) in col y, advance down a row
			y = 0
			x = x + 1
		else:
			y = y + 1
		return x,y
	def retreat(x,y):
		if y == 0: # row position 0 in col y, retreat up a row
			y = n - 1
			x = x - 1
			if x < 0:
				x = 0
		else:
			y = y - 1
		return x,y
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
			elif op in ['!']:
				mini_val = target
			if mini_val == target:
				# print('mini ',this_mini,' is correct')
				return 1
			else:
				# print('mini ',this_mini,' is INCORRECT')
				return 0



	# initialize variables
	allvals = np.array(range(1,n+1)) # e.g. [1,2,3,4] for n = 4 puzzle
	x = 0
	y = 0
	moves  = 0

	# loop through puzzle grid
	while x <= n-1 and y <= n-1:
		# newturn()
		# print("start of turn val: ",puzzle[x,y])
		validval = available(x,y)
		# print("valid values: ",validval)
		if validval.size == 0: # no legal move at x,y
			puzzle[x,y] = 0
			x,y = retreat(x,y)
			continue
		else: # legal moves exist
			validbool = validval >= puzzle[x,y]
			if puzzle[x,y] == 0:
				puzzle[x,y] = np.min(validval)
			elif (0 < puzzle[x,y] < n) and (validbool.sum() > 0):
				puzzle[x,y] = np.min(validval[validbool])
			else:
				puzzle[x,y] = 0
				x,y = retreat(x,y)
				continue

		if full_mini(x,y): # current mini is full, proceed to mini check
			mini_index = minis[x,y]
			if mini_check(mini_index,operators[mini_index],targets[mini_index]):
				# print('mini %d is correct'%(mini_index))
				x,y = advance(x,y)
			else: 
				# print('mini %d is INCORRECT'%(mini_index))
				continue
		else:
			# print("end of turn val: ",puzzle[x,y])
			x,y = advance(x,y)
		moves = moves + 1

		if moves % 1000 == 0:
			newturn()

	win()
	return puzzle



