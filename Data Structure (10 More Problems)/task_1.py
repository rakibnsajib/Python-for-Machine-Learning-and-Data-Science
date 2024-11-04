# Example 1: Nested Lists Operations
# List is a collection which is ordered and changeable. Allows duplicate members.
# Nested list is a list that can contain any sort object, even another list (sublist), which in turn can contain sublists themselves, and so on.
# Working with nested lists by accessing the elements, modifying values, and flttening the list.

# Example nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in nested list
print("Accessing elements in nested list")
print(nested_list[1][2])

# Modifying values in nested list
print("Modifying values in nested list")
nested_list[1][2] = 10 # Change the value of 6 to 10
print(nested_list)

# Flattening the list
print("Flattening the list")
flattened_list = [element for sublist in nested_list for item in sublist for element in (item if isinstance(item, list) else [item])]
print(flattened_list)