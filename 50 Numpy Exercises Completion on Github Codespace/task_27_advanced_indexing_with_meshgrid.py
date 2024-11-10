# Example 27: NumPy - Advanced Indexing with Meshgrid
# Advanced indexing with `np.meshgrid()` in NumPy allows generating coordinate grids that can be used to index and manipulate arrays for multi-dimensional operations.

import numpy as np

# Creating 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5])

# Creating meshgrid for advanced indexing
X, Y = np.meshgrid(x, y)
indices = np.vstack([X.ravel(), Y.ravel()])

print('Indices for Meshgrid Advanced Indexing:\n', indices)
