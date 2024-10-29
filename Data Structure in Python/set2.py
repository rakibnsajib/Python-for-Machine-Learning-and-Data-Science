# Example 2: Adding Elements to a Set
# You can add elements to a set using the add() and update() methods.
# Sets do not allow duplicate elements. If you try to add an element that is already present in the set, it will not be added again.

# Example Set
my_set = {1, 2, 3, 4}

# Add an element to the set
my_set.add(5)

# Try to add an element that is already present in the set (it will not be added)
my_set.add(3)

# Print the updated set
print('Updated Set (add method):', my_set)

# Add multiple elements to the set using the update() method
my_set.update([6, 7, 8])

# Print the updated set
print('Updated Set (update method):', my_set)