# Example 25: NumPy - Masked Indexing with np.ma.masked_where
# The `np.ma.masked_where()` function in NumPy creates a masked array where elements satisfying a given condition are masked (ignored) in calculations or operations.

import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# Masking elements where values are negative
masked_array = np.ma.masked_where(array < 0, array)

print('Masked Array with Negative Values Hidden:', masked_array)