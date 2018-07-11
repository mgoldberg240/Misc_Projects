import numpy as np
import kenken as kk
from timeit import default_timer as timer




# ### SAMPLE PUZZLE 1
# n = 4
# puzzle = np.zeros([n,n])
# puzzle = puzzle.astype(int)

# minis = [0,0,1,1,2,3,3,1,4,3,3,5,4,6,6,5]
# minis = np.array(minis)
# minis = np.reshape(minis,[n,n])
# minis = minis.astype(int)

# op = ['/','+','!','*','-','/','+']

# targets = [2,7,4,12,2,2,5]

# p1 = kk.solve(n,puzzle,minis,op,targets)



# # ### SAMPLE PUZZLE 2
# n = 4
# puzzle = np.zeros([n,n])
# puzzle = puzzle.astype(int)

# minis = [0,0,1,1,2,0,1,3,2,4,5,5,4,4,6,6]
# minis = np.array(minis)
# minis = np.reshape(minis,[n,n])
# minis = minis.astype(int)

# op = ['*','+','-','!','*','/','/']

# targets = [16,7,2,4,12,2,2]

# p2 = kk.solve(n,puzzle,minis,op,targets)



# # ## SAMPLE PUZZLE 3
# n = 6
# puzzle = np.zeros([n,n])
# puzzle = puzzle.astype(int)

# minis = [0,1,1,2,3,3,0,4,4,2,5,3,6,6,7,7,5,3,6,6,8,9,10,10,11,11,8,9,9,12,13,13,13,14,14,12]
# minis = np.array(minis)
# minis = np.reshape(minis,[n,n])
# minis = minis.astype(int)

# op = ['+','/','*','*','-','/','*','*','*','+','*','*','+','+','/']

# targets = [11,2,20,6,3,3,240,6,6,7,30,6,9,8,2]

# p3 = kk.solve(n,puzzle,minis,op,targets)



## SAMPLE PUZZLE 4
n = 9
puzzle = np.zeros([n,n])
puzzle = puzzle.astype(int)

minis = [0,0,1,1,2,3,3,4,4,5,5,6,6,2,7,3,8,9,10,10,11,11,11,7,12,8,9,13,14,14,15,15,16,12,12,17,13,18,19,19,16,16,20,20,21,13,18,18,22,22,23,24,24,21,25,26,26,27,28,23,29,30,30,25,25,27,27,28,31,29,29,30,32,32,27,33,33,31,34,35,35]
minis = np.array(minis)
minis = np.reshape(minis,[n,n])
minis = minis.astype(int)

op = '**-**/-*+--**++-*!*+-/+/-*-***+-/*!+'
op = list(op)

targets = [35,12,4,216,8,4,4,42,10,8,2,72,48,17,17,4,25,4,84,17,5,2,3,2,3,42,8,864,28,108,12,1,4,40,2,16]

p4 = kk.solve(n,puzzle,minis,op,targets)

