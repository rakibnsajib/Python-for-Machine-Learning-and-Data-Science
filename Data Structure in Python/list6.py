# Example 6: List Slicing
# List slicing is used to extract a part of a list by specifying a range of indices.
# It is done using the colon (:) operator to specify the start, stop, and step indices.
# Syntax: list[start:stop:step]

# Example List
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the list from index 2 to 5
sliced_list1 = my_list[2:6]

# Slice the list from index 0 to 8 with a step of 2
sliced_list2 = my_list[0:9:2]

# Print the sliced lists
print('Sliced List 1:', sliced_list1)
print('Sliced List 2:', sliced_list2)