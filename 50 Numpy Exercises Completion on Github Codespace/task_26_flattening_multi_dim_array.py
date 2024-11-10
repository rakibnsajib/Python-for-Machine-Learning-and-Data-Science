# Example 26: NumPy - Flattening a Multi-dimensional Array
# Flattening a multi-dimensional array in NumPy involves converting it into a one-dimensional array.
# Functions like `ravel()` and `flatten()` are used for this purpose.

import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Flattening the array
flattened_array = array_2d.flatten()

print('Flattened Array:', flattened_array)