# Example 5: Removing Elements from a List
# You can remove elements from a list using the remove() and pop() methods.
# The remove() method removes the first occurrence of a specified value from the list.
# Syntax: list.remove(value)
# The pop() method removes the element at the specified index and returns it.
# Syntax: list.pop(index)

# Example List
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Remove the element 'c' from the list
my_list.remove('c')

# Pop the element at index 3
popped_element = my_list.pop(3)

# Print the modified list and the popped element
print('Modified List:', my_list)
print('Popped Element:', popped_element)

