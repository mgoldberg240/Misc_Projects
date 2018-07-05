# This file doesn't do much if anything
# was meant for testing the mini check function

n = 4 # width of puzzle
sample = np.zeros(n**2)
sample[4] = 4

minis = [0,0,1,1,2,3,3,1,4,3,3,5,4,6,6,5]
minis = np.array(minis)
minis = np.reshape(minis,[n,n])

puzzle = [2,4,3,1,4,2,1,3,1,3,2,4,3,1,4,2]
puzzle = np.array(puzzle)
puzzle = np.reshape(puzzle,[n,n])

op = ['/','+','','*','-','/','+']

targets = [2,7,4,12,2,2,5]


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
		return 1
	else:
		return 0


for i in range(0,7):
	mini_check(minis,i,sol,op[i],targets[i])