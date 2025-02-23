# In the previous two exercises, you developed functions that convert
# simple numeric strings to signed integers. In this exercise and the
# next, you're going to reverse those functions.

# Write a function that converts a non-negative integer value (e.g., 0,
# 1, 2, 3, and so on) to the string representation of that integer.

# You may not use any of the standard conversion functions available in
# Python, such as str. Your function should do this the old-fashioned
# way and construct the string by analyzing and manipulating the number.


'''
P
input: a non-negative integer
output: the string version of the same number
rules:
    explicit:
        - do NOT use str()
        -
    implicit:
        - need to handle the edge case of 0

E
4321 % 10 = 1
4321 // 10 = 432
432 % 10 = 2
432 // 10 = 43
43 % 10 = 3
43 // 10 = 4
4 % 10 = 4

D
list of string integers (index matches integer to string counterpart)

A
- create a list of string integers to map index to string
- initialize an empty string
- if number is zero, string should equal 0
- otherwise, while number is greater than zero, take number % 10 and
front append the result to the string, converted to its string counterpart
- return the string number
'''


def integer_to_string(num):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    if num == 0:
        result += '0'
    else:
        while num > 0:
            digit = num % 10
            result = numbers[digit] + result
            num = num // 10
    return result


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
