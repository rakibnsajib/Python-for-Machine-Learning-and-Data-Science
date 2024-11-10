# Example 19: NumPy - Clipping Array Values
# The `np.clip()` function in NumPy limits the values in an array to a specified range, replacing values below or above the range with the defined minimum and maximum values.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Clipping values to be between 2 and 4
clipped_array = np.clip(array, 2, 4)

print('Original Array:', array)
print('Clipped Array:', clipped_array)
