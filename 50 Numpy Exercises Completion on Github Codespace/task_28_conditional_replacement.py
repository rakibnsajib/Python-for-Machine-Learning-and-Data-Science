# Example 28: NumPy - Conditional Replacement with np.where
# The `np.where()` function in NumPy allows conditional replacement of array elements, returning a new array with values chosen based on a specified condition.

import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Replacing values based on condition
result = np.where(array > 20, 0, array)

print('Array with Values Greater Than 20 Replaced with 0:', result)