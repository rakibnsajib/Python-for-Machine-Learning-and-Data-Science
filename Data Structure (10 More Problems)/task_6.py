# Example 6: Set Operations with Multiple Sets
# Set is a collection which is unordered and unindexed. No duplicate members.
# Performing union, intersection, and symmetric difference with three sets using set operations.

# Example Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 6, 7, 8}

# Performing set operations
union_set = set1.union(set2, set3)
intersection_set = set1 & set2 & set3
symmetric_difference_set = set1 ^ set2 ^ set3

# Displaying the results
print('Union of Sets:', union_set)
print('Intersection of Sets:', intersection_set)
print('Symmetric Difference of Sets:', symmetric_difference_set)