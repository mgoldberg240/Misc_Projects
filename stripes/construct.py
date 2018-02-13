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

N = 10
O = 0
cell = unit(N,O)



#cell = shift(cell,'r',N,O)
cell = shift(cell,'r',N,O)
cell = shift(cell,'r',N,1)
cell = shift(cell,'r',N,O)
cell = shift(cell,'r',N,1)


# print(cell)

# print(cell.shape)



plot_cells(cell,N)

# The letter 'A'
# ///////////
# ////\\\////
# ////\\\////
# ///////////
# ///\\\\\///
# ///\\\\\///
# ///\\\\\///
