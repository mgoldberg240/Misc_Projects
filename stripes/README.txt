Created by Matthew Goldberg on Feb 9th, 2018 in Python 3.6

Stripes Project:
—Create text using striped patterns. e.g. we draw the letter 'S' (looks the same as the number 2) like so:

\\\\\\\\\\\\\\\
\\\/////////\\\
\\\///\\\///\\\
\\\///\\\///\\\
\\\\\\\\\///\\\
\\\/////////\\\
\\\///\\\\\\\\\
\\\///\\\///\\\
\\\///\\\///\\\
\\\/////////\\\
\\\\\\\\\\\\\\\

-Diagonal lines in one direction make up the letters, while diagonal lines in the other direction make up the blank space between letters
-Line density (number of diagonal lines in a unit square) can be changed with parameter N

# ~——————————~ #
# CURRENT CODE #
# ~——————————~ #

unit.py			Generate unit cells: [/] or [\]
shift.py		Copy + Paste existing cells to create new ones
cell_plot.py		Plot cell data
construct.py		Assemble a design using cell_plot.plot_cells()
			    -Currently just a way to test the plot command

# ~——————————~ #
# FUTURE  CODE #
# ~——————————~ #

alphabet.py		Convert strings of letters/words to pattern arrangments
construct.py		By the end, one should be able to type plot_cells('word') and get 			out the entire word written in the striped pattern

