# Write a function that takes a string, doubles every character in the
# string, then returns the result as a new string.

'''
P
input: a string
output: a new string with every character doubled

E

D

A
- for each character in the string, add it twice to a new string
- return the new string
'''

def repeater(string):
    new_string = ''
    for char in string:
        new_string += f'{char}{char}'
    return new_string

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
