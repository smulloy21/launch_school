# Write a function that takes a list of positive integers as input,
# multiplies all of the integers together, divides the result by the
# number of entries in the list, and returns the result as a string
# with the value rounded to three decimal places.

'''
P
input: a list of positive integers
output: a string of the average of the integers, rounded to 3 decimal places
rules:
    explicit:
        - output should be a string
        - output should be rounded to 3 decimal places
    implicit:
        - don't need to worry about empty input or input other than a list of integers

E
multiplicative_average([3, 5]) == "7.500"
(3 * 5) / 2 = 7.5
7.5 => "7.500"

D

A
- take the product of the list, and divide it by the length of the list.
- coerce the result to a string, and format it to only include the first 3 decimal places
'''
import math

def multiplicative_average(lst):
    result = math.prod(lst) / len(lst)
    return f'{result:.3f}'


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
