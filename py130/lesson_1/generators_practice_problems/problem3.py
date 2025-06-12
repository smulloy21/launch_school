# Use a generator expression to capitalize every string in a list of strings.
# Use a single print invocation to print all the capitalized strings as a
# tuple.

capitalized = (word.capitalize() for word in ['for', 'the', 'fjords'])

print(tuple(capitalized))
