# Example 13: NumPy - Statistical Functions
# NumPy provides statistical functions like `mean`, `median`, `std`, and `var` to compute measures such as average, standard deviation, and variance across arrays or specific axes.

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Calculating statistical values
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)
variance = np.var(array)

print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)
print('Variance:', variance)