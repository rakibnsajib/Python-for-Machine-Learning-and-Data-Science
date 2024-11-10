# Example 29: NumPy - Using np.choose for Multiple Conditions
# The `np.choose()` function in NumPy selects elements from multiple arrays based on index arrays,
# enabling conditional selection and element replacement for complex scenarios.

import numpy as np

# Creating an array for conditions
array = np.array([0, 1, 2, 3])

# Creating conditions based on the array
choices = [array * 2, array + 10, array ** 2]

# Create an index array that specifies which choice to pick for each element of the array
# For example, we can use a condition based on the values of `array` to decide which choice to pick
# Let's assume we want to select:
# - `array * 2` for elements less than 2
# - `array + 10` for elements equal to 2
# - `array ** 2` for elements greater than 2

index = np.select([array < 2, array == 2, array > 2], [0, 1, 2])

# Using np.choose to apply different conditions
result = np.choose(index, choices)

print('Result using np.choose:', result)
