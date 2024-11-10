# Example 18: NumPy - Advanced Slicing with Step in 2D Array
# Advanced slicing with step in a 2D array allows extracting specific patterns or subarrays by specifying a step value for rows and columns using the slicing syntax [start:stop:step].

import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Slicing every second element in rows and columns
result = array_2d[::2, ::2]

print('Advanced Sliced Array with Step:\n', result)
