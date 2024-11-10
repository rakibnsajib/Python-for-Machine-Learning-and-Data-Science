# Example 15: NumPy - Concatenation of Arrays
# NumPy provides functions like `np.concatenate()` to join arrays along a specified axis.
# Other functions like `np.vstack()` and `np.hstack()` enable vertical and horizontal stacking.

import numpy as np

# Creating arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Concatenating arrays
concatenated_array = np.concatenate((array1, array2))

print('Concatenated Array:', concatenated_array)
