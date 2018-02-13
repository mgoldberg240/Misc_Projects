import numpy as np
import unit
import matplotlib.pyplot as plt
from shapely.geometry import LineString

make_tuple = unit.make_tuple
unit = unit.unit

def plot_cells(coord_array,N):
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# 			   		   plot cells 	 			 		#
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# coord_array	  : type --- ndarray			    	#
	# 			  	  - array of all existing coordinates 	# 
	# ----------------------------------------------------- #
	# N    		  	  : type --- positive integer		   	#
	# 			 	  - number of lines across unit cells  	# 
	# ----------------------------------------------------- #
	fig, ax = plt.subplots()

	coord_array = make_tuple(coord_array)

	for row in range(0,len(coord_array),2):
		line_coords = [coord_array[row],coord_array[row+1]]
		line = LineString(line_coords)
		x,y = line.coords.xy
		#fig, ax = plt.subplots()
		ax.plot(x, y, color='k',linewidth=1, solid_capstyle='round', zorder=2)
		# ax.set_title('unit cell with ' + str(N) + ' stripes')
	
	plt.show()
	fig.clf()