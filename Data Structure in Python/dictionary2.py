# Example 2: Accessing Dciaonary Values
# Values in a dictionary can be accessed using their keys.
# If a value is not found, a KeyError is raised unless you use the get() method, which returns the default value None if the key is not found.

# Example Dictionary
my_dict = {'name': 'Elon', 'age': 26, 'city': 'Los Angeles'}

# Accessing Values using keys
name = my_dict['name']
age = my_dict.get('age')

# Print the accessed values
print('Name:', name)
print('Age:', age)
