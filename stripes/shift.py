import numpy as np
import unit
import matplotlib.pyplot as plt
from shapely.geometry import LineString
unit = unit.unit

# As of Feb 13, shift needs to use the orientation 'O' parameter 
# How can you invert any cell given its coordinates?

# r -> [N,0]
# L -> [-N,0]
# U -> [0,N]
# D -> [0,-N]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# 			   		   shift cells 	 			 		#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# coord_array	  : type --- ndarray			    	#
# 			  	  - array of all existing coordinates 	# 
# ----------------------------------------------------- #
# direction    	  : type --- string		 			  	#
# 			 	  - number of lines across unit cells  	# 
# ----------------------------------------------------- #

def shift(coord_array,direction,N,O):
	if direction in ['right','Right','RIGHT','r','R']:
		shift_array = [N,0]
	elif direction in ['left','Left','LEFT','l','L']:
		shift_array = [-N,0]
	elif direction in ['up','Up','UP','u','U']:
		shift_array = [0,N]
	elif direction in ['down','Down','DOWN','d','D']:
		shift_array = [0,-N]

	lC = 4*N-2 # number of coordinates in a cell (lC = length of cell)
	shift = np.array([shift_array]*lC)
	# print('shift')
	# print("")
	# print(shift)
	shift = coord_array[-lC:,:] + shift

	# invert orientation of a cell
	def invert(coord_array,N):
		coord_array[:,0] = -coord_array[:,0] + N
		return coord_array
	if O == 1:
		shift = invert(shift,N)	

	combined = np.vstack([coord_array,shift]) # append new coordinates to bottom
	return combined
