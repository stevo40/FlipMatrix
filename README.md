# FlipMatrix
This is an experiment to make matrices which can be transposed more efficiently as this can be an inefficient function.

The matrix is sliced into diagonal form and stored in memory.

The coordinates can then be converted from (x,y) to (diagonal row, position in diagonal row) coordinates.

To transpose the data we can either:
1. Reverse the list of diagonal rows

or

2. Change the coordinate formula which we are looking at.


Note: Using the data in this format can be inefficient.

For example:
1. Multiplication. If we already have columns and rows stored in cloned arrays, multiplying these is straightforward as we need to iterate both arrays at the same time in memory to get the result. Here the data is scattered so can be a more complex process.
2. Array access: requires formula to convert between x,y and diagonal object, position in object.
