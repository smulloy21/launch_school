# Create a function that takes a list of numbers, all of which are the same
# except one. Find and return the number in the list that differs from all
# the rest.

# The list will always contain at least 3 numbers, and there will always be
# exactly one number that is different.

"""
P
input: a list of repeating numbers, with one other number
output: the one outlying number in the list

E

D

A
option1, option2 = set(lst)
- use a set to narrow down to the two number options
- iterate over the first 3 elements in the array
- use a dict to get a count, with option1 and option2 as keys
- whichever has a count of one, is the outlier, return it

"""

def what_is_different(lst):
    option1, option2 = set(lst)
    count = {option1: 0, option2: 0}
    for i in range(len(lst)):
        count[lst[i]] += 1
    for option in count:
        if count[option] == 1:
            return option

# Examples
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
# The above tests should each print True.
