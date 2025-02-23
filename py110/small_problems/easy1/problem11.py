# In the previous exercise, you developed a function that converts
# non-negative numbers to strings. In this exercise, you're going to
# extend that function by adding the ability to represent negative
# numbers as well.

# Write a function that takes an integer and converts it to a string
# representation.

# You may not use any of the standard conversion functions available in
# Python, such as str. You may, however, use integer_to_string from the
# previous exercise.


'''
P
input: a positive, negative, or 0 integer
output: a string representation of that integer
rules:
    explicit:
        - you cannot use str()
        - you can use the function from the previous exercise
    implicit:
        - positive numbers should be led by '+', negative integers by '-'
        and 0 by neither

E

D

A
if integer is > 0:
    return the result of the previous function, led by '+'
if integer is < 0:
    return the result of the previous function with its absolute value, led by '-'
else:
    return '0'
'''


def signed_integer_to_string(integer):
    if integer > 0:
        return '+' + integer_to_string(integer)
    elif integer < 0:
        return '-' + integer_to_string(abs(integer))
    else:
        return '0'


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


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
