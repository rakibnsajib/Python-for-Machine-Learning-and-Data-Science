# Example 10: Tuple Comprehension using Generator Expression
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Creating a tuple using a generator expression for elements that meet a condition.

# Example range of numbers
numbers = range(10)

# Creating a tuple of squares for squares of even numbers
even_squares = tuple(x**2 for x in numbers if x % 2 == 0)

print('Tuple of Squares for Even Numbers:', even_squares)