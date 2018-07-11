import numpy as np
import unit
import matplotlib.pyplot as plt
from shapely.geometry import LineString
unit = unit.unit

def shift_right(cell_coords,N,O):
	cell_coords = unit(N,O) # return array of coordinates
	shift = np.array([[N,0]]*lC)
	total = cell_coords+shift
	new_tup = tuple(map(tuple,total))
	return new_tup


totalTup = cTup + shiftTup

# def shift_left(cell_coords,):

# def shift_up(cell_coords,):

# def shift_down(cell_coords,):