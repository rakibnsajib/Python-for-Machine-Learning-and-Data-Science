# Example 7: NumPy - Reshaping Arrays
# Reshaping in NumPy changes the shape of an array without altering its data.
# The `reshape()` function adjusts the dimensions while maintaining the total number of elements.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Reshaping to different dimensions
reshaped_array = array.reshape((2, 3))

print('Original Array:', array)
print('Reshaped Array:\n', reshaped_array)