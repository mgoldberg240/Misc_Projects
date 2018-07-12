import numpy as np

size = 4
arr = np.arange(size**2)
arr = np.random.permutation(arr).reshape((size,size))
print(arr)