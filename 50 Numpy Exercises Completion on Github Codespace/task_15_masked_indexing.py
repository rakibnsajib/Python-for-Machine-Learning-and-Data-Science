# Example 15: NumPy - Masked Indexing
# Masked indexing in NumPy involves using a boolean mask to select or modify specific elements in an array.
# Masks can be created based on conditions applied to the array.

import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# Creating a mask for positive values
mask = array > 0

# Applying mask to get only positive values
positive_values = array[mask]

print('Positive Values:', positive_values)