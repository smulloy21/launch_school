# Create a function that takes a nonempty string as an argument and returns a
# tuple consisting of a string and an integer. If we call the string argument
# s, the string component of the returned tuple t, and the integer component
# of the tuple k, then s, t, and k must be related to each other such that
# s == t * k. The values of t and k should be the shortest possible substring
# and the largest possible repeat count that satisfies this equation.

# You may assume that the string argument consists entirely of lowercase
# alphabetic letters.

"""
P
input: a string, potentially consisting of a substring repeated n times
output: the shortest possible substring, and the integer n
rules:
- all characters are lowercase and alphabetic

E

xyzxyzxyz
x
xy
xyz

D

A
high-level:
- while getting all substrings:
- if replacing the substring in the string with a non-alpha character, creates a non-alpha string
-- then we have the smallest substring, and the count of the non-alpha character is n
- else if we complete the loop, the string itself is the largest substring and n = 1

"""

def repeated_substring(string):
    placeholder = '*'
    for i in range(1, len(string) + 1):
        substring = string[0:i]
        replaced = string.replace(substring, placeholder)
        if len(set(replaced)) == 1:
            return (substring, replaced.count(placeholder))

# Examples
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
# The above tests should each print True.
