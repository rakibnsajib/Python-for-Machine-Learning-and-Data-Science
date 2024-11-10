# Example 8: NumPy - Transposing Arrays
# Transposing in NumPy rearranges the dimensions of an array.
# The `transpose()` function or `.T` attribute is used to swap axes in a multidimensional array.

import numpy as np

# Creating a 2D array
array = np.array([[1, 2], [3, 4]])

# Transposing the array
transposed_array = np.transpose(array)

print('Original Array:\n', array)
print('Transposed Array:\n', transposed_array)