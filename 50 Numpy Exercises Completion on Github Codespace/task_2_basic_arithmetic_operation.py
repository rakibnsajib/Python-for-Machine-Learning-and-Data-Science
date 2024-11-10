# Example 2: NumPy - Basic Arithmetic Operations
# NumPy provides basic arithmetic operations that can be performed element-wise on arrays.
# These operations include addition, subtraction, multiplication, division, and exponentiation.

import numpy as np

# Creating arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Arithmetic operations
added = np.add(array1, array2)
subtracted = np.subtract(array1, array2)
multiplied = np.multiply(array1, array2)
divided = np.divide(array1, array2)

print('Added:', added)
print('Subtracted:', subtracted)
print('Multiplied:', multiplied)
print('Divided:', divided)