# Example 9: NumPy - Multi-dimensional Slicing
# Multi-dimensional slicing in NumPy extracts specific sections from arrays across multiple dimensions.
# It uses the syntax [start:stop:step] for each dimension, separated by commas.


import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Multi-dimensional slicing
sub_array = array_2d[1:, 1:3]

print('Sub Array (Slicing Rows and Columns):\n', sub_array)