# Example 9: Dictionary Filtering Based on Conditions
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Filtering a dictionary to retain only key-value pairs that satisfy a certain condition.

# Example dictionary
scores = {'Alice': 70, 'Bob': 85, 'Charlie': 64, 'David': 90, 'Eve': 75}

# Filtering to retain scores >= 80
filterd_scores = {name: score for name, score in scores.items() if score >= 80}

print('Filtered Scores: ', filterd_scores)
