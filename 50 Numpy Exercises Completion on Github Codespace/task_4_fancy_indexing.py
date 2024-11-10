# Example 4: NumPy - Fancy Indexing
# Fancy indexing in NumPy allows accessing array elements using arrays of indices

import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Selecting specific indices
selected_elements = array[[1, 3, 4]]

print('Selected Elements:', selected_elements)