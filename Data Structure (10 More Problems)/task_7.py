# Example 7: Dictionary with Nested Structures
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Acccesing and modifying nested elements in a dictionary with nested structures.

# Example dictionary with nested structures
nested_dict = {
    'person1': {
        'name': 'John',
        'details': {
            'age': 30,
            'city': 'New York',
            'skills': ['Python', 'Java', 'C++']
        }
    },
    'person2': {
        'name': 'Alice',
        'details': {
            'age': 25,
            'city': 'San Francisco',
            'skills': ['JavaScript', 'Ruby', 'Go']
        }
    }
}

# Accessing elements in nested dictionary
city = nested_dict['person1']['details']['city']


# Modifying a nested element in a dictionary
nested_dict['person1']['details']['skills'].append('SQL')

print('City: ', city)
print('Updated Nested Dictionary: ', nested_dict)
