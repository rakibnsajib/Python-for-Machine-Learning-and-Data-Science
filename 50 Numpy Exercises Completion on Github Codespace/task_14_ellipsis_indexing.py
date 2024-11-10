# Example 14: NumPy - Using Ellipsis (...) in Indexing
# The ellipsis (`...`) in NumPy indexing represents selecting all elements along unspecified dimensions.
# It simplifies indexing for multi-dimensional arrays, especially when not all axes need to be explicitly defined.

import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Using ellipsis to select all elements along specific axes
result = array_3d[..., 1]  # Selecting the second column in each 2D slice

print('Result using Ellipsis (...):\n', result)