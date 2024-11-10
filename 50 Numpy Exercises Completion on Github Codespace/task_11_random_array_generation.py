# Example 11: NumPy - Random Array Generation
# NumPy provides the `np.random` module to generate random arrays.
# Functions like `rand`, `randn`, `randint`, and `random` create arrays with random values based on uniform, normal, or other specified distributions.

import numpy as np

# Generating random arrays
random_array = np.random.rand(3, 3)  # Random values in a 3x3 array
normal_array = np.random.randn(3, 3)  # Random values with a normal distribution

print('Random Array:\n', random_array)
print('Normal Distribution Array:\n', normal_array)