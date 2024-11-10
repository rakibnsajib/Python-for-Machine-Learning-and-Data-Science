# Example 10: NumPy - Sorting Arrays
# NumPy provides functions like `np.sort()` and `argsort()` for sorting arrays.
# Sorting can be done along a specific axis or the flattened array, in ascending or descending order.

import numpy as np

# Creating an array
array = np.array([3, 1, 2, 5, 4])

# Sorting the array
sorted_array = np.sort(array)

print('Original Array:', array)
print('Sorted Array:', sorted_array)