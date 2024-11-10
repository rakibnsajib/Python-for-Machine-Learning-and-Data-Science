
# Example 6: NumPy - 3D Array Indexing
# A 3D array is a collection of 2D arrays arranged in a third dimension (depth).
# Indexing a 3D array involves specifying indices for depth, row, and column to access elements.

import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Accessing elements in a 3D array
element = array_3d[1, 0, 1]  # Accessing the element at [1, 0, 1]

# Slicing in 3D
slice_3d = array_3d[:, 0, :]

print('Element at (1,0,1):', element)
print('Sliced 3D Array:\n', slice_3d)
