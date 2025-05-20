# Create a function that takes two string arguments and returns the number of
# times that the second string occurs in the first string. Note that
# overlapping strings don't count: 'babab' contains 1 instance of 'bab', not
# 2.

# You may assume that the second argument is never an empty string.

"""
P
input: two string arguments
output: the number of times the second string occurs int he first string
rules:
- overlapping does not count
- the second argument is never empty

E

D

A
- split first string by the second string
- return the length of the list -1

"""

def count_substrings(string1, string2):
    lst = string1.split(string2)
    return len(lst) - 1

# Examples
print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
# The above tests should each print True.
