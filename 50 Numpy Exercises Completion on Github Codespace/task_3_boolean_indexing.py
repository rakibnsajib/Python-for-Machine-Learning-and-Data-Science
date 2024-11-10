# Example 3: NumPy - Boolean Indexing
# Boolean indexing in NumPy is a technique to filter and select elements from an array
# using a boolean array or a condition. It allows retrieval of elements that satisfy a given condition.

import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Boolean indexing
greater_than_20 = array[array > 20]

print('Elements Greater Than 20:', greater_than_20)
