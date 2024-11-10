# Example 5: NumPy - Trigonometric Functions
# NumPy provides trigonometric functions like `sin`, `cos`, and `tan`
# for performing element-wise computations of trigonometric values on arrays.
# It also includes inverse functions (`arcsin`, `arccos`, `arctan`) and angle conversions.

import numpy as np

# Creating an array
angles = np.array([0, np.pi/2, np.pi])

# Trigonometric functions
sin_array = np.sin(angles)
cos_array = np.cos(angles)
tan_array = np.tan(angles)

print('Sine of Angles:', sin_array)
print('Cosine of Angles:', cos_array)
print('Tangent of Angles:', tan_array)