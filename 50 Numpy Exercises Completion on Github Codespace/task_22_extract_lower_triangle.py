# Example 22: NumPy - Extract Lower Triangle of a Matrix
# The `np.tril()` function in NumPy extracts the lower triangle of a matrix, setting all elements above the main diagonal to zero.

import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the lower triangle (below the main diagonal)
lower_triangle = np.tril(matrix)

print('Lower Triangle of the Matrix:\n', lower_triangle)