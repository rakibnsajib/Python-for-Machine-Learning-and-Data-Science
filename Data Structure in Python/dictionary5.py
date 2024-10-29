# Example 5: Removing Key-Value Pairs from a Dictionary
# You can remove key-value pairs from a dictionary using the del keyword or the pop() method.
# The del keyword removes the key-value pair with the specified key from the dictionary.
# The pop() method removes the key-value pair with the specified key and returns the value.
# Also clear() method can be used to remove all the key-value pairs from the dictionary.

# Example Dictionary
my_dict = {'name': 'Elon', 'age': 26, 'city': 'Los Angeles'}

# Remove a key-value pair using del keyword
del my_dict['age']

# Print the updated dictionary
print('Updated Dictionary (del method):', my_dict)

# Remove a key-value pair using pop() method
city = my_dict.pop('city')

# Print the updated dictionary
print('Updated Dictionary (pop method):', my_dict)
print('Removed Value:', city)

# Remove all key-value pairs using clear() method
my_dict.clear()

# Print the updated dictionary
print('Updated Dictionary (clear method):', my_dict)