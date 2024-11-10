# Example 8: NumPy - Conditional Indexing
# Conditional indexing in NumPy allows selecting or modifying array elements based on conditions.
# It involves applying a condition to the array, resulting in a boolean mask for element selection.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Setting elements that satisfy a condition
array[array % 2 == 0] = -1  # Set even numbers to -1

print('Array after Conditional Indexing:', array)