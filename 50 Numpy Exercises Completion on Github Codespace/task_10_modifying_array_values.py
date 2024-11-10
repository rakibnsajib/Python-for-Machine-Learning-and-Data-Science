# Example 10: NumPy - Modifying Array Values using Indexing
# In NumPy, array values can be modified using indexing by directly assigning new values to specific elements or slices of the array based on their indices.

import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Modifying values at specific indices
array[[1, 3]] = [100, 200]

print('Modified Array:', array)