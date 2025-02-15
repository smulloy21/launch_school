# Given the following string, create a dictionary that represents the
# frequency with which each letter occurs. The frequency count should
# be case-sensitive:

statement = "The Flintstones Rock"

# The output should resemble the following:

# Pretty printed for clarity
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}

# Your program may output the pairs in a different order.

output = {char: statement.count(char) for char in statement if not char.isspace()}
print(output)
