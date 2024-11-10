# Example 2: NumPy - 2D Array Indexing
# A 2D array is a grid-like data structure with rows and columns, where each element is accessed using two indices.
# Indexing refers to accessing individual elements, while slicing involves extracting subsets of rows or columns.

import numpy as np

# Initialize a 2D array
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Accessing a specific element (row 1, column 2)
element = array_2d[1, 2]

# Extracting slices
first_row = array_2d[0, :]        # All columns in the first row
second_column = array_2d[:, 1]    # All rows in the second column

# Displaying results
print('Element at (1,2):', element)
print('First Row:', first_row)
print('Second Column:', second_column)
