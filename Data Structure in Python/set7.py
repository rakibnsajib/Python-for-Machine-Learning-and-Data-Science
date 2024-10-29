# Example 7: Set Symmetric Difference
# The symmetric_difference() method returns the symmetric difference between two sets.
# The symmetric difference between two sets is the elements that are present in either set, but not in both sets.
# You can also use the ^ operator to find the symmetric difference between two sets.

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the symmetric difference between set1 and set2
symmetric_difference_set = set1.symmetric_difference(set2)

# Print the symmetric difference
print('Symmetric Difference of Sets (using symmetric_difference method):', symmetric_difference_set)

# Find the symmetric difference using the ^ operator
symmetric_difference_set = set1 ^ set2

# Print the symmetric difference
print('Symmetric Difference of Sets (using ^ operator):', symmetric_difference_set)