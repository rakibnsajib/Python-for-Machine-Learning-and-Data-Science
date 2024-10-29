# Example 6: Set Difference
# The difference() method returns the difference between two sets. The difference between two sets is the elements that are present in the first set but not in the second set.
# You can also use the - operator to find the difference between two sets.

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the difference between set1 and set2 (elements in set1 but not in set2)
difference_set = set1.difference(set2)

# Print the difference
print('Difference of Sets (using difference method):', difference_set)

# Find the difference using the - operator
difference_set = set1 - set2

# Print the difference
print('Difference of Sets (using - operator):', difference_set)