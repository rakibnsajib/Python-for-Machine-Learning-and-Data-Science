# Example 8: List Comprehension with Conditional Nesting
# List is a collection which is ordered and changeable. Allows duplicate members.
# Using list comprehension with nested loops and conditions to filter elements.

# Example Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flattening and filtering even numbers from the matrix
even_flattened = [num for row in matrix for num in row if num % 2 == 0]

print('Flattened List with Even Numbers:', even_flattened)