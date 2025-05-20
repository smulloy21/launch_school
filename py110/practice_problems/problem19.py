# Create a function that takes a list of integers as an argument and returns
# the integer that appears an odd number of times. There will always be
# exactly one such integer in the input list.

"""
P
input: a list of integers
output: the one integer that appears an odd number of times in the input list
rules:
- there will always be exactly one such integer in the input list

E

D

dict?

A
- iterate through the list, for each element:
-- if it's count in the list is odd:
--- return that element
"""

def odd_fellow(lst):
    seen_nums = set()
    for num in lst:
        if num in seen_nums:
            continue
        if lst.count(num) % 2 == 1:
            return num
        else:
            seen_nums.add(num)

# Examples
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
# The above tests should each print True.
