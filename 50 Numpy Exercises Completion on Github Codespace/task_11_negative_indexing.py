# Example 11: NumPy - Indexing with Negative Indices
# Negative indexing in NumPy allows accessing elements from the end of an array.
# The last element is indexed as -1, the second-to-last as -2, and so on.

import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Accessing elements from the end using negative indices
last_element = array[-1]
second_last_element = array[-2]

print('Last Element:', last_element)
print('Second Last Element:', second_last_element)