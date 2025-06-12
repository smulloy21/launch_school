# Define a function named concat_strings that takes any number of strings and
# returns the concatenation of all the strings. Add a keyword-only argument
# sep with a default value of ' ' that specifies the separator to use between
# the strings.

def concat_strings(*args, sep=' '):
    return sep.join(args)

print(concat_strings("Hello", "world!"))              # Hello world!
print(concat_strings("one", "two", "three", sep='+')) # one+two+three
