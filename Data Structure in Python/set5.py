# Example 5: Set Intersection
# The intersection() method returns the intersection of two sets. The intersection of two sets is the elements that are common to both sets.
# You can also use the & operator to find the intersection of two sets.

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the intersection of set1 and set2 (common elements in both sets)
intersection_set = set1.intersection(set2)

# Print the intersection
print('Intersection of Sets (using intersection method):', intersection_set)

# Find the intersection using the & operator
intersection_set = set1 & set2

# Print the intersection
print('Intersection of Sets (using & operator):', intersection_set)