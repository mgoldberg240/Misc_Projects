Created by Matthew Goldberg on June 11 2018 (Happy Birthday Alex!)


kenken.py

Solve a kenken puzzle using backtracking

a kenken (square grid of size n x n) is solved when:
	(1) all minis (see below) are solved
	(2) all rows contain integers between 1 and n with no repeats
	(3) all columns contain integers between 1 and n with no repeats

Example puzzle: consider the 4 x 4 grid
[0 0 0 0]
[4 0 0 0]
[0 0 0 0]
[0 0 0 0]
Cell [0,1] contains a 4. This value is a given, and will remain unchanged

Minis: Chunks/groups of adjacent grid squares within puzzle, each paired with some operation. Numbers within a mini solve an equation using said operator. Solutions of each equation are given by target values

In our example puzzle, the minis are given by
[0 0 1 1]
[2 3 3 1]
[4 3 3 5]
[4 6 6 5],

paired with operators

[/,+,(given),*,-,/,+],

and targets

[2,7,4,12,2,2,5].

To clarify, mini 3 is given by the four central grid squares. These four values must multiply out to target value 12 in order for the puzzle to be complete. A mini is 'full' when it contains all non-zeros values, at which point we evaluate the associated equation.


The solving algorithm used is basic backtracking. Beginning with position [x,y] = [0,0] (top left of puzzle), a test value is input such that is does not violate the given row and column constraints (say this value is 1). In the following position [0,1], another value is tested, say 2. If the value passes the row and column tests, and the local mini is 'full', it is subject to the 'mini_check'. Note that in our example, mini 0, which is comprised of [0,0] and [0,1], so it is full. If a row check, column check, or mini check fails, we erase the current value, retreat back one position, and test a value new to that position. We repeat this process until the whole grid is full.

for this example, the solution is
[2,4,3,1]
[4,2,1,3]
[1,3,2,4]
[3,1,4,2]




