# Example 20: NumPy - Extracting Upper Triangle of a Matrix
# The `np.triu()` function in NumPy extracts the upper triangle of a matrix, setting all elements below the main diagonal to zero.

import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the upper triangle (above the main diagonal)
upper_triangle = np.triu(matrix)

print('Upper Triangle of the Matrix:\n', upper_triangle)