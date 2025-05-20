# Create a function that takes a list of integers as an argument and returns a
# tuple of two numbers that are closest together in value. If there are
# multiple pairs that are equally close, return the pair that occurs first in
# the list.

"""
P
input: a list of integers
output: a tuple of two numbers from the list that are closest together in value.
rules:
- if there are multiple pairs that are equally close, return the pair that occurs first
in the list

E
closest_numbers([12, 22, 7, 17]) == (12, 7)
(12, 7) (12, 17)

(0, 1) (0, 2) (0, 3)
(1, 2) (1, 3)
(2, 3)

i range(0, len - 2)
j in range (i + 1, len - 1)

D

A
- get all the pairs HELPER
- find the pair that has the lowest absolute difference
- if multiple pairs have the same lowewst absolute difference, return the first

- HELPER all_pairs: i in range 0 to len - 2, j in range 1 to len - 1

"""

def all_pairs(lst):
    return [(lst[i], lst[j]) for i in range(len(lst) - 1) for j in range(i + 1, len(lst))]

def closest_numbers(lst):
    pairs = sorted(all_pairs(lst), key=lambda x: abs(x[0] - x[1]))
    return pairs[0]

# ALTERNATIVE:
# def closest_numbers(lst):
#     min_diff = float('inf')
#     result = None

#     for i in range(len(lst) - 1):
#         for j in range(i + 1, len(lst)):
#             diff = abs(lst[i] - lst[j])
#             if diff < min_diff:
#                 min_diff = diff
#                 result = (lst[i], lst[j])

#     return result

# Examples
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
# The above tests should each print True.
