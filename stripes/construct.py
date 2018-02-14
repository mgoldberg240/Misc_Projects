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


cell = unit(N,O)
print(cell)




for i in range(2,5):
	cell = shift(cell,'r',N,1)
cell = shift(cell,'r',N,0)
cell = shift(cell,'d',N,0)
for i in range(2,5):
	cell = shift(cell,'l',N,1)
cell = shift(cell,'l',N,0)


plot_cells(cell,N)

# The letter 'A'
# ///////////
# ////\\\////
# ////\\\////
# ///////////
# ///\\\\\///
# ///\\\\\///
# ///\\\\\///
