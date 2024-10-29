# Example 7: List Comprehension
# List comprehension is a concise way to create lists using an expression and iteration.
# Syntax: [expression for item in iterable]
# Syntax: [expression for item in iterable if condition]
# It can be used to create a list from an existing list, a range, or any other iterable object.

# Create a list of squares of numbers from 1 to 5
squared_list = [x**2 for x in range(1, 6)]

# Create a list of even numbers from 1 to 10
even_list = [x for x in range(1, 11) if x % 2 == 0]

# Print the lists
print('Squared List:', squared_list)
print('Even List:', even_list)