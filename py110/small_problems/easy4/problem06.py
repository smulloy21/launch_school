# Write a function that takes a string argument and returns a list of
# substrings of that string. Each substring should begin with the first
# letter of the word, and the list should be ordered from shortest to
# longest.


'''
P
input: a string
output: a list of all substrings starting from the first character

E

D

A
list comprehension of all the substrings concatinating from the first character
'''


# def leading_substrings(string):
#     lst = []
#     s = ''
#     for char in string:
#         s += char
#         lst.append(s)
#     return lst


def leading_substrings(string):
    return [string[:i + 1] for i in range(len(string))]


# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
