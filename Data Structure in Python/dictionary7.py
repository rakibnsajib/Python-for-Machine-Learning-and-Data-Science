# Example 7: Checking Membership in a Dictionary
# You can the membership of a key in a dictionary using the 'in' and 'not in' operators.

# Example Dictionary
my_dict = {'name': 'Elon', 'age': 26, 'city': 'Los Angeles'}

# Check if a key is present in the dictionary
if 'name' in my_dict:
    print('Key "name" is present in the dictionary')
else:
    print('Key "name" is not present in the dictionary')

# Check if a key is not present in the dictionary
if 'country' not in my_dict:
    print('Key "country" is not present in the dictionary')
else:
    print('Key "country" is present in the dictionary')