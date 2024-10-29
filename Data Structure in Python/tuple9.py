# Example 9: Sorting a Tuple
# Tuples are immutable and can not be sorted directly.
# To sort a tuple, you need to convert it to a list, sort the list, and then convert it back to a tuple.

# Example tuple
num_tuple = (5, 2, 8, 6, 3, 1, 7, 4)

# Sort the tuple by converting it to a list
sorted_list = sorted(num_tuple) # sorted() returns a new sorted list

# Convert the list back to a tuple
sorted_tuple = tuple(sorted_list)

# Print the sorted tuple
print('Sorted Tuple:', sorted_tuple)