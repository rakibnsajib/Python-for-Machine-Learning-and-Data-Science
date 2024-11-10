# Example 3: NumPy - Power and Square Root
# NumPy provides functions for power and square root operations.
# The `np.power()` function computes the power of each element in an array,
# and the `np.sqrt()` function computes the square root of each element.

import numpy as np

# Creating an array
array = np.array([1, 4, 9, 16])

# Power and square root
squared = np.power(array, 2)
sqrt = np.sqrt(array)

print('Squared Array:', squared)
print('Square Root of Array:', sqrt)
