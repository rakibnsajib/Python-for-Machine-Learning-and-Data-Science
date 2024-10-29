# Example 3: Tuple Immutability
# Tuples are immutable, meaning their values cannot be changed after creation.
# Trying to modify a tuple will result in an error.

# Example tuple
my_tuple = (1, 2, 3)

# Trying to modify an element (this will raise an error)
try:
    my_tuple[1] = 10
except TypeError as e:
    print('Error:', e)