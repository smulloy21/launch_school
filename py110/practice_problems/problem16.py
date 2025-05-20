# Create a function that returns the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the
# input string. You may assume that the input string contains only
# alphanumeric characters.

"""
P
input: a string of alphanumeric characters
output: the count of unique (case insesitive) chars and digits that appear more than once in the input

E

D

A
- initialize `distinct_multiples_count` to 0
- initialize `seen_chars` to an empty dict
- for each character in the casefolded string,
-- if it is present in the `seen_chars` dict
--- if it its value is 1
---- increment `distinct_multiples_count`
--- increment its value in `seen_chars` by 1
-- else
--- add it to the `seen_chars` dict
- return `distinct_multiples_count

"""

def distinct_multiples(string):
    distinct_multiples_count = 0
    seen_chars = {}
    for char in string.casefold():
        if char in seen_chars:
            if seen_chars[char] == 1:
                distinct_multiples_count += 1
            seen_chars[char] += 1
        else:
            seen_chars[char] = 1
    return distinct_multiples_count

# Examples
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
# The above tests should each print True.
