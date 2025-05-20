# Create a function that takes a list of numbers as an argument. For each
# number, determine how many numbers in the list are smaller than it, and
# place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values. That is, if a number
# occurs multiple times in the list, it should only be counted once.


"""
P
input: a list of numbers
output: a list of numbers, representing hope many unique numbers in the
original list are smaller than each given number in the input
rules:
- only count a number once (we want only unique numbers for the less than
comparison)

E
smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]


D
- a set? for uniqueness

A
- get the length of the set of unique lower numbers for each number in the
input list
"""

def smaller_numbers_than_current(numbers):
    return [len({num for num in numbers if num < i}) for i in numbers]

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
# The above tests should each print True.
