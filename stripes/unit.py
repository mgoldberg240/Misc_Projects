import numpy as np

def make_tuple(coord_array):
	# convert coordinate array to tuple for use of shapely.geometry.LineString()
	return tuple(map(tuple,coord_array))

def unit(n,o):
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# 			   	 Generate unit cells 				 	#
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# n    		  : number of nodes/length of cells			#
	#     		  - type: positive integer			    	#
	# 			  - number of lines across unit cells  		# 
	# ----------------------------------------------------- #
	# o    		  : cell orientation 						#
	#     		  - type: boolean							#
	#             - 0 implies left orientation: [/]		 	#
	#             	diagonals go lower left to upper right  #
	#													 	#
	#             - 1 implies right orientation: [\]  	    #
	#             	diagonals go upper left to lower right  #	
	# ----------------------------------------------------- #
	
	# prepare diagonal coordinates
	# constructions between [/] and [\] are quite similar, little corrections occur throughout
	
	# B refers to diagonals that have at least one coordinate at the bottom of the unit cell
	Bxx =  np.arange(0,n)
	Bxy = np.array([0]*n)

	if o == 1:
		Bxx = Bxx+1
	Bx = np.vstack((Bxx,Bxy)).T

	if o == 1:
		By = np.flip(Bx,1)
	else:
		By = np.flip(n-Bx,1)

	B = np.hstack([Bx,By])
	B = B.reshape(2*n,2)

	# T refers to diagonals that have at least one coordinate at the top of the unit cell
	# e.g those left over after B is constructed
	m = n-1
	Txx = np.arange(1,n)
	Txy = np.array([n]*m)
	Tx = np.vstack((Txx,Txy)).T
	if o == 1:
		Ty = np.flip(Tx,1)
	else:
		Ty = np.flip(n-Tx,1)
	T = np.hstack([Tx,Ty])
	T = T.reshape(2*m,2)	

	# concatenate bottom and top coord, convert to coordinate tuple
	coords = np.vstack([B,T])

	# coords can be returned as tuples for easy use with shapely.geometry.LineString()
	# coords = tuple(map(tuple,coords))

	return coords
