# Write a function that takes a string argument consisting of a first
# name, a space, and a last name. The function should return a new
# string consisting of the last name, a comma, a space, and the first
# name.

# You may assume that the names don't include middle names, initials,
# or suffixes ("Jr.", "Sr.").

'''
P
input: a string containing first name, a space, and last name
output: a string containing last name, a comma, a space, and first name
rules:
    explicit:
        - don't worry about middle names, initials, or suffixes

E

D

A
- unpack the split of the string into first and last name
- string format into the required last name, comma, space, first name
'''


def swap_name(full_name):
    first, last = full_name.split()
    return f'{last}, {first}'


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
