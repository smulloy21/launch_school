# Write a function that computes the difference between the square of
# the sum of the first count positive integers and the sum of the
# squares of the first count positive integers.

"""
P
input: a positive integer
output: the difference of the square of the sums of those integers and the sum of the squares of the integers

E
sum_square_difference(3) == 22
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

D

A
- create a list of the range from 1 to input integer
- get the square of the sums by summing the list and returning its square
- get the sum of squares by transforming the list to its square values and then summing it
- return the difference of the sum of squares from the square of sums and return it

"""


def sum_square_difference(count):
    nums = [i for i in range(1, count + 1)]
    square_of_sums = sum(nums)**2
    sum_of_squares = sum([num**2 for num in nums])
    return square_of_sums - sum_of_squares


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
