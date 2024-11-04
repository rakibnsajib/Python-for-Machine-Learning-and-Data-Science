# Example 5: List of Tuples to Dictionary
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Converting a list of tuples into a dictionary using a loop

# Example list of tuples
tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Converting list of tuples into dictionary
result_dict = {key: value for key, value in tuple_list}

print('Dictionary from List of Tuples:', result_dict)
