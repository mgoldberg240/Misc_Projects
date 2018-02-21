import numpy as np
import operator
import unit
import shift
import cell_plot
import matplotlib.pyplot as plt
from shapely.geometry import LineString

unit = unit.unit
shift = shift.shift

plot_cells = cell_plot.plot_cells

N = 5
O = 0


cell = unit(N,1)


xmax = 6
ymax = 7
xmin = 1
ymin = 1

for i in range(xmin,xmax):
	cell = shift(cell,'r',N,1)
# for i in range(ymin,ymax):
# 	cell = shift(cell,'d',N,1)
# for i in range(xmin,xmax):
# 	cell = shift(cell,'l',N,1)
# for i in range(xmin,xmax-1):
# 	cell = shift(cell,'u',N,1)

plot_cells(cell,N)

# The letter 'A'
# ///////////
# ////\\\////
# ////\\\////
# ///////////
# ///\\\\\///
# ///\\\\\///
# ///\\\\\///

# //////
# //\\//
# //////
# //\\//
# //\\//
# //\\//