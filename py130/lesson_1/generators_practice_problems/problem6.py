# Create a generator function that generates the capitalized version of every
# string in a list of strings whose length is less than 5. Use a single print
# invocation to print all the capitalized strings as a set.

words = ['the', 'itsy', 'bitsy', 'spider']

def capitalized(words):
    for word in words:
        if len(word) < 5:
            yield word.capitalize()

print(set(capitalized(words)))
