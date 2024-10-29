# Example 3: Removing Elements from a Set
# You can remove elements from a set using the remove() method. If the element is not present in the set, a KeyError is raised.
# You can also use the discard() method to remove an element from a set. The discard() method removes the element if it is present; otherwise, it does nothing.

# Example set
my_set = {1, 2, 3, 4, 5}

# Remove an element from the set using remove()
my_set.remove(3)

# Print the updated set
print('Set after removing an element:', my_set)

# Try to remove an element that is not present in the set
# This will raise a KeyError
try:
    my_set.remove(6)
except KeyError:
    print('KeyError: Element not found in the set')

# Remove an element from the set using discard()
my_set.discard(5)

# Print the updated set
print('Set after removing another element:', my_set)