# Example 16: NumPy - Splitting Arrays
# The `np.array_split()` function in NumPy splits an array into multiple subarrays.
# Unlike `np.split()`, it allows unequal divisions if the array cannot be evenly split.


import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Splitting the array into three parts
split_arrays = np.array_split(array, 3)

print('Split Arrays:', split_arrays)