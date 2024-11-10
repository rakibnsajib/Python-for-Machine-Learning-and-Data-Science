# Example 23: NumPy - Multi-dimensional Array Indexing with Mixed Types
# Multi-dimensional array indexing with mixed types in NumPy combines integer, slice, and boolean indexing.
# It allows flexible access to specific elements, subarrays, or conditional selections within arrays.

import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Mixing slicing with direct indexing
mixed_index = array_3d[1:, 0, 1]

print('Mixed Type Indexing Result:', mixed_index)