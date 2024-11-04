# Example 4: Dictionary Merging with Comprehension
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Merging two dictionaries and modifying the values using dictionary comprehension.

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# Merging two dictionaries using dictionary comprehension
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

print('Merged and Modified Dictionary:', merged_dict)
