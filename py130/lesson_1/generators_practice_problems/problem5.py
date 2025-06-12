# Use a generator expression to capitalize the strings in a list of strings
# whose length is at least 5. Use a single print invocation to print all the
# capitalized strings as a set.

words = ['the', 'itsy', 'bitsy', 'spider']

capitalized = (word.capitalize() for word in words if len(word) >= 5)

print(set(capitalized))
