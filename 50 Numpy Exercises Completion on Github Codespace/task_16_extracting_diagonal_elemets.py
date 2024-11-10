# Example 16: NumPy - Extracting Diagonal Elements
# NumPy provides the `np.diag()` function to extract diagonal elements from a 2D array
# or from specified diagonals of a higher-dimensional array.

import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the main diagonal
diagonal_elements = np.diag(matrix)

print('Diagonal Elements:', diagonal_elements)