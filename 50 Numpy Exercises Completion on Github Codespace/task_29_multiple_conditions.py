# Example 29: NumPy - Using np.choose for Multiple Conditions
# The `np.choose()` function in NumPy selects elements from multiple arrays based on index arrays,
# enabling conditional selection and element replacement for complex scenarios.

import numpy as np

# Creating arrays for conditions
array = np.array([0, 1, 2, 3])
choices = [array*2, array+10, array**2]

# Using np.choose to apply different conditions
result = np.choose(array, choices)

print('Result using np.choose:', result)
