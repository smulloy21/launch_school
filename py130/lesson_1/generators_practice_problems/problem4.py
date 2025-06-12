# Create a generator function that generates the capitalized version of every
# string in a list of strings. Use a single print invocation to print all the
# capitalized strings as a tuple.

def capitalized():
    for word in ['for', 'the', 'fjords']:
        yield word.capitalize()

print(tuple(capitalized()))
