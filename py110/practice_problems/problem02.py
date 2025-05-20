# Create a function that takes a list of integers as an argument. The function
# should return the minimum sum of 5 consecutive numbers in the list. If the
# list contains fewer than 5 elements, the function should return None.

"""
P
input: a list of integers
output: the minimum sum of 5 consecutive numbers in the list, or None, if less
than 5 elements

E
minimum_sum([1, 2, 3, 4, 5, -5]) == 9
1, 2, 3, 4, 5 (sum = 15)
2, 3, 4, 5, -5 (sum = 9)

D

A
- if the input list has less than 5 elements, return None
- for the range 5 to the length of the list + 1, get the sum of that slice of the list.
- return the minimum sum

"""

def minimum_sum(numbers):
    if len(numbers) < 5:
        return None

    sums = [sum(numbers[i-5: i]) for i in range(5, len(numbers) + 1)]
    return min(sums)

# Examples
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
# The above tests should each print True.
