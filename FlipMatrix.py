class FlipMatrix:

    # FlipMatrix structure:
    matrix = []

    size_x = 0
    size_y = 0

    def to_store(self, arr):
        '''
        \n    Convert a 2d matrix into diagonal row form and store as local "matrix"
        \n    This will turn:
        \n    [1, 2]
        \n    [3, 4]
        \n    into:
        \n    [2]
        \n    [1, 4]
        \n    [3]
        '''

        # Destination:
        output = []

        # A queue of rows to iterate
        # This will make the conversion process easier.
        working = []

        # How many iterations have we tried?
        iterations_looped = 0

        # Initial set up.
        # Put first matrix row on the queue:
        working.append(arr[0])
        # Set up with first matrix row length:
        loc_in_first = len(arr[0])-1

        self.size_x = len(arr[0])
        self.size_y = len(arr)


        # While we have a line in the working queue:
        while len(working) > 0:

            # Break early for debug:
            #if iterations_looped > 7:
            #    break

            #print("Row to process: " + str(iterations_looped))

            # row to generate:
            new_row = []

            # Use loc in first as a starting offset:
            offset = 0 + loc_in_first

            # go through rows in the current queue:
            for working_row_pos in range(len(working)):
                #print(str(working_row_pos) + " : " + str(midloc))
                # We are going to add diagonal elements to our new row.
                new_row.append(working[working_row_pos][offset])
                # Add one so the offset in the next row is diagonal:
                # next position will be one down, one to the right
                offset = offset + 1

            # Diagonal complete, add to the output:
            output.append(new_row)

            # This will either
            if loc_in_first == 0:
                # Remove the first row in the working queue
                working.pop(0)
            else:
                # or shift start position of the diagonal one to the left.
                loc_in_first = loc_in_first - 1

            #print(loc_in_first)

            # Update the number of iterations:
            iterations_looped = iterations_looped + 1

            # While we still have rows not added to the queue
            if iterations_looped < len(arr):
                # Add row to the queue
                working.append(arr[iterations_looped])


        self.matrix = output
        #print(output)

    def convert_coordinates(self, local_x, local_y):
        '''
            Convert x, y into diagonal form:

        :param x: The X coordinate
        :param y: The Y coordinate
        :return: Return coordinates as tuple (diagonal array position, pos in diagonal array).
        '''

        row = 0
        pos_in_row = 0

        if (local_x >= local_y):
            pos_in_row = local_y
        else:
            pos_in_row = local_x

        x_size = self.size_x - 1

        row = x_size - local_x + local_y

        return_cord = (row, pos_in_row)

        return return_cord

    def value_at_coordinate(self, x, y):
        loc = self.convert_coordinates(x, y)
        row = loc[0]
        pos_in_row = loc[1]
        value = self.matrix[row][pos_in_row]
        #print(str(row) + " " + str(pos_in_row) + " " + str(value))
        return value

    def transpose(self):
        #self.matrix = \
        self.matrix.reverse()
        copy_x = self.size_x
        self.size_x = self.size_y
        self.size_y = copy_x


# Dev code:
arr_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
f = FlipMatrix()
f.to_store(arr_in)
print(f.matrix)

for y in range(4):
    for x in range(3):
        cord = f.convert_coordinates(x, y)
        value = f.value_at_coordinate(x, y)
        print(str(x) + "\t" + str(y) + "\t\t" + str(cord[0]) + "\t" + str(cord[1]) + "\t" + str(value))

print("")

f.transpose()

for y in range(3):
    for x in range(4):
        cord = f.convert_coordinates(x, y)
        value = f.value_at_coordinate(x, y)
        print(str(x) + "\t" + str(y) + "\t\t" + str(cord[0]) + "\t" + str(cord[1]) + "\t" + str(value))


#val = f.value_at_coordinate(0, 0)
#print(val)