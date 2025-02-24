# Write a function that takes an integer argument and returns a list
# containing all integers between 1 and the argument (inclusive), in
# ascending order.

# You may assume that the argument will always be a positive integer.

'''
P
input: an integer
output: a list containing all integers from 1 to the argument, inclusive
rules:
    explicit:
        - the argument will always be a positive integer

E

D

A
- initialize a new list
- for index in range from 1 to integer + 1, append index to list
- return the list
'''


def sequence(integer):
    return [num for num in range(1, integer + 1)]


print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
