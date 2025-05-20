# Create a function that takes a single integer argument and returns the sum
# of all the multiples of 7 or 11 that are less than the argument. If a number
# is a multiple of both 7 and 11, count it just once.

# For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21,
# and 22. The sum of these multiples is 75.

# If the argument is negative, return 0.

"""
P
input: a single integer
output: the sum of all the multiples of 7 or 11 that are less than the argument
rules:
- if a number is a multiple of both 7 and 11, count it only once

E

D

A
- set comprehension to get all the unique multiples of 7 or 11, under the input integer
- return the sum of the set

"""

def seven_eleven(num):
    multiples = {i for i in range(0, num) if i % 7 == 0 or i % 11 == 0}
    return sum(multiples)

# Examples
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
# The above tests should each print True.
