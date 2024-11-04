# Example 3: Set Comprehension
# Set is a collection which is unordered and unindexed. No duplicate members.
# Set comprehension is a concise way to create sets using a single line of code.
# Creating a set using comprehension with a condition to filter specific elements.

# Example Set
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creating a set of even numbers using set comprehension
even_set = {num for num in numbers if num % 2 == 0}

print('Set of Even Numbers: ', even_set)