# Create a function that takes a list of integers as an argument and returns
# the number of identical pairs of integers in that list. For instance, the
# number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both
# 2 and 1.

# If the list is empty or contains exactly one value, return 0.

# If a certain number occurs more than twice, count each complete pair once.
# For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should
# return 2. The first list contains two complete pairs while the second has an
# extra 2 that isn't part of the other two pairs.

"""
P
input: a list of integers
output: an integer, representing the number of pairs of integers in the given list
rules:
- if the list is empty or has one value, return 0
- count complete pairs only once. ie, if there are three instances of an integer, it is only one pair

E

D

A
- create a set of the list, to get only unigue integer values, named `unique_integers`
- create a counter `pairs` set to 0
- for each number in `unique_integers`, count the number of times it occurs in the list, divided by 2
-- add that 'number of pairs` to the counter `pairs`
- return `pairs`

"""

def pairs(lst):
    pair_count = 0
    unique_integers = set(lst)
    for num in unique_integers:
        num_pairs = lst.count(num) // 2
        pair_count += num_pairs
    return pair_count

# Examples
print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
# The above tests should each print True.
