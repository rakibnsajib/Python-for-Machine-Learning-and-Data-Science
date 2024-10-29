# Example 7: Tuple Comprehension (Using Generator Expression)
# Tuples do not support comprehension like lists.
# However, you can use a generator expression to create a tuple.

# Create a tuple of squares of numbers from 1 to 5
squares_tuple = tuple(x**2 for x in range(1, 6))

# Print the tuple of squares
print('Tuple of Squares:', squares_tuple)