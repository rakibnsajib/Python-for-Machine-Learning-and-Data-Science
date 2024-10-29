# Example 5: Removing Elements from a Tuple
# Tuples are immutable, so you cannot remove elements from a tuple directly.
# To remove an element from a tuple, you can convert the tuple to a list, remove the element, and then convert the list back to a tuple.

# Example tuple
my_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a list
temp_list = list(my_tuple)
temp_list.remove(3)
my_tuple = tuple(temp_list)

# Print the updated tuple after removing an element
print('Tuple after removing an element:', my_tuple)