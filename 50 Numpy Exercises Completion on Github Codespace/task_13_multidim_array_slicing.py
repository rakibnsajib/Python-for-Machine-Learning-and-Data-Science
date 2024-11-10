# Example 13: NumPy - Indexing Multi-dimensional Arrays with Slices
# Indexing multi-dimensional arrays with slices in NumPy allows selecting subarrays using slice objects ([start:stop:step]) along each axis, enabling efficient data extraction.

import numpy as np

# Creating a 3x4 array
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Selecting specific rows and columns using slices
selected_slice = array_2d[1:, :2]

print('Selected Slice:\n', selected_slice)