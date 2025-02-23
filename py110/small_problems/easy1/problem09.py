# In the previous exercise, you developed a function that converts
# simple numeric strings to integers. In this exercise, you're going to
# extend that function to work with signed numbers.

# Write a function that takes a string of digits and returns the
# appropriate number as an integer. The string may have a leading
# + or - sign; if the first character is a +, your function should
# return a positive number; if it is a -, your function should return a
# negative number. If there is no sign, return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion functions available in
# Python, such as int. You may, however, use the string_to_integer
# function from the previous exercise.


'''
P
input: a string number, which may or may not have a leading + or - sign
output: the integer version of the number
rules:
    explicit:
        - do NOT use int() to convert
        - you CAN use your function from the previous question
        - if the string has a leading + sign, return a positive integer
        - if the string has a leading - sign, return a negative integer


E

D

A
- if there is a leading - sign, save to a variable that negative = True
- remove any leading signs from the string
- convert the string to its positive integer using the previous function
- if negative = True, subtract twice of the number from itself
- return the number
'''


# def string_to_signed_integer(string):
#     negative = False
#     if string[0] in ('+', '-'):
#         if string[0] == '-':
#             negative = True
#         string = string[1:]
#     integer = string_to_integer(string)
#     if negative:
#         integer -= integer*2
#     return integer


def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)


def string_to_integer(string_number):
    values = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    sum = 0
    places = reversed(list(string_number))
    for idx, num in enumerate(places):
        sum += values[num] * (10**idx)
    return sum


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
