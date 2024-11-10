# Example 21: NumPy - Reverse Array using Indexing
# NumPy allows reversing an array using slicing with a negative step, which flips the order of elements along a specific axis.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Reversing the array using slicing
reversed_array = array[::-1]

print('Reversed Array:', reversed_array)