# Example 4: Set Union
# The union() method returns the union of two sets.
# The union of two sets is a new set that contains all elements from both sets.
# You can also use the | operator to find the union of two sets.

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the union of set1 and set2 (all elements from both sets)
union_set = set1.union(set2)

# Print the union
print('Union of Sets (using union method):', union_set)

# Find the union using the | operator
union_set = set1 | set2

# Print the union
print('Union of Sets (using | operator):', union_set)