# Example 9: Sorting a List
# The sort() method sorts the list in ascending order by default.
# You can sort the list in descending order by passing the argument reverse=True to the sort() method.

# Example List
number_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sort the list in ascending order
number_list.sort()
print('Sorted List in Ascending Order:', number_list)

# Sort the list in descending order
number_list.sort(reverse=True)
print('Sorted List in Descending Order:', number_list)