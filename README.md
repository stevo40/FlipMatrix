# FlipMatrix
This is an experiment to make matrices which can be transposed more efficiently as this can be an inefficient function.

The matrix is sliced into diagonal form and stored in memory.

The coordinates can then be converted from (x,y) to (diagonal row, position in diagonal row) coordinates.

To transpose the data we can either:
1. Reverse the list of diagonal rows

or

2. Change the coordinate formula which we are looking at.
