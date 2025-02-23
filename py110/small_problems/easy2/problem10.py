# Write a function that takes one argument, a list of integers, and
# returns the average of all the integers in the list, rounded down to
# the integer component of the average. The list will never be empty,
# and the numbers will always be positive integers.

'''
P
input: a list of positive integers
output: the average of the list, rounded down to the integer component of the average

E

D

A
- get the mathmatical average of the list (the product of the list divided by its length)
- use integer division so the result is an int
'''


def average(lst):
    return sum(lst) // len(lst)


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
