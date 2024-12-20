# Example 7: NumPy - Indexing with Arrays
# Indexing with arrays in NumPy allows selecting elements using arrays of integer or boolean indices, enabling advanced and flexible data selection from one or more dimensions.

import numpy as np

# Creating a 2D array
array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Using arrays for indexing
rows = np.array([0, 1, 2])
cols = np.array([2, 1, 0])
indexed_elements = array_2d[rows, cols]

print('Indexed Elements:', indexed_elements)