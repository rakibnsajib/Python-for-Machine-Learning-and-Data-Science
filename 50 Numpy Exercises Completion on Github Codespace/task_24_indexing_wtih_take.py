# Example 24: NumPy - Indexing with np.take
# The `np.take()` function in NumPy retrieves elements from an array along a specified axis using an array of indices, allowing advanced and flexible element selection.

import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Using np.take to select elements at specific indices
indices = [0, 2, 4]
result = np.take(array, indices)

print('Selected Elements using np.take:', result)