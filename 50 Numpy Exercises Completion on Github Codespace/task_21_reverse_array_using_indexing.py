# Example 21: NumPy - Reverse Array using Indexing
# Reversing an array in NumPy can be done using slicing with a step of -1, which iterates through the array elements in reverse order.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Reversing the array using slicing
reversed_array = array[::-1]

print('Reversed Array:', reversed_array)