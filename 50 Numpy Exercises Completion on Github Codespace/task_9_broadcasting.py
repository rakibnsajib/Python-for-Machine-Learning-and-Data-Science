# Example 9: NumPy - Broadcasting
# Broadcasting in NumPy allows arithmetic operations between arrays of different shapes by automatically expanding their dimensions to be compatible for element-wise operations.

import numpy as np

# Creating an array
array = np.array([1, 2, 3])

# Broadcasting: Adding a scalar to an array
result = array + 10

print('Original Array:', array)
print('Array after Broadcasting:', result)