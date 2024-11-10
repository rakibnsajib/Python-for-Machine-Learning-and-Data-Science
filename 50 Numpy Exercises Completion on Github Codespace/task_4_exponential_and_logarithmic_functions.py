# Example 4: NumPy - Exponential and Logarithmic Functions
# NumPy provides functions for exponential and logarithmic computations.
# The `np.exp()` function computes the exponential of each element in an array.
# Logarithmic functions like `np.log()`, `np.log10()`, and `np.log2()` compute natural, base-10, and base-2 logarithms, respectively.

import numpy as np

# Creating an array
array = np.array([1, 2, 3])

# Exponential and logarithmic functions
exp_array = np.exp(array)
log_array = np.log(array)

print('Exponential of Array:', exp_array)
print('Logarithm of Array:', log_array)