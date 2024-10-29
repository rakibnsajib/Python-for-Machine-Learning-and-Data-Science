# Example 6: Tuple Slicing
# Slicing allows you to extract a part of a tuple.
# It is done using a colon (:) to specify the start, stop, and step indices.
# Syntax: tuple[start:stop:step]

# Example tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slice the tuple from index 2 to index 5
slice_tuple = my_tuple[2:6]

# Print the sliced tuple
print('Sliced Tuple:', slice_tuple)

# Slice the tuple from index 0 to index 8 with a step of 2
slice_tuple = my_tuple[0:9:2]

# Print the sliced tuple
print('Sliced Tuple (step 2):', slice_tuple)