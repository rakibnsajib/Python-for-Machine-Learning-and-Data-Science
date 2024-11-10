# Example 14: NumPy - Unique Elements and Counting
# NumPy provides functions like `np.unique()` to find unique elements in an array

import numpy as np

# Creating an array with duplicate values
array = np.array([1, 2, 2, 3, 4, 4, 4, 5])

# Finding unique elements and their counts
unique_elements, counts = np.unique(array, return_counts=True)

print('Unique Elements:', unique_elements)
print('Counts of Unique Elements:', counts)