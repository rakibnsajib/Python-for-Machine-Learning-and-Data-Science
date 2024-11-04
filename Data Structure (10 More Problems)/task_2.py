# Example 2: Tuple Unpacking
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple unpacking is a way to assign the elements of a tuple to a sequence of variables.
# Unpacking a tuple with multiple values into variables, including using the * operator for remaining values.

# Example tuple
person_info = ('John', 30, 'New York', 'Engineer', 'Single')

# Unpacking a tuple into variables
name, age, *other_info = person_info

print("Unpacking a tuple into variables")
print('Name:', name)
print('Age:', age)
print('Other Information:', other_info)