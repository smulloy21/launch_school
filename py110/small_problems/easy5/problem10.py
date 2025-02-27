# Given a sequence of integers, filter out instances where the same
# value occurs successively, retaining only the initial occurrence.
# Return the refined sequence.


'''
P
input: a list of integers
output: the list with successive same values removed

E

D

A
- list comprehension for index in list, keep the value only if it is not the same as the previous one
'''


def unique_sequence(lst):
    return [num for idx, num in enumerate(lst) if lst[idx-1] != num]


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
