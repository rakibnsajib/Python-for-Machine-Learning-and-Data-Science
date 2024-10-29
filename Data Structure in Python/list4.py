# Example 4: Adding elements to a list
# You can add elements to a list using the append() or insert() methods.
# The append() method adds an element to the end of the list, while the insert() method adds an element at a specific index.
# The insert() method takes two arguments: the index at which to insert the element and the element to insert.

# Example list
my_list = [1, 2, 3, 4, 5]

# Add an element to the end of the list
my_list.append(6)

# Add an element at a specific index
my_list.insert(2, 7)

# Print the modified list
print('Modified list:', my_list) # Output: [1, 2, 7, 3, 4, 5, 6]