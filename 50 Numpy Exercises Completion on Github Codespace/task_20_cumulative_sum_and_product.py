# Example 20: NumPy - Cumulative Sum and Product
# NumPy provides `np.cumsum()` to calculate the cumulative sum
# and `np.cumprod()` to calculate the cumulative product of array elements along a specified axis.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4])

# Calculating cumulative sum and product
cumulative_sum = np.cumsum(array)
cumulative_product = np.cumprod(array)

print('Cumulative Sum:', cumulative_sum)
print('Cumulative Product:', cumulative_product)