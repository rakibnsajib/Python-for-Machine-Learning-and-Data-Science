# Example 9: Merging Dictionaries
# You can merge two dictionaries using the update() method or the ** operator.

# Example Dictionaries
dic1 = {'name': 'Elon', 'age': 26}
dic2 = {'city': 'Los Angeles', 'country': 'USA'}

# Merge the dictionaries using the update() method
dic1.update(dic2)

# Merge the dictionaries using the ** operator
dic3 = {**dic1, **dic2}

# Print the merged dictionaries
print('Merged Dictionary (update):', dic1)
print('Merged Dictionary (**):', dic3)