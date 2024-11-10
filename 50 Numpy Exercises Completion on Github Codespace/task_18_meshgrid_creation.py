# Example 18: NumPy - Meshgrid Creation
# The `np.meshgrid()` function in NumPy creates coordinate grids from one-dimensional arrays.
# It is used for evaluating functions over a grid of points in multi-dimensional spaces.

import numpy as np

# Creating 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Creating a meshgrid
X, Y = np.meshgrid(x, y)

print('Meshgrid X:\n', X)
print('Meshgrid Y:\n', Y)