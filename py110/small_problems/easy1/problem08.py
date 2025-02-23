# Write a function that takes a string of digits and returns the
# appropriate number as an integer. You may not use any of the standard
# conversion functions available in Python, such as int. Your function
# should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you
# worry about invalid characters; assume all characters are numeric.

'''
P
input: a string of digits
output: the integer version of the number
rules:
    explicit:
        - do NOT use int() to convert
        - do not worry about invalid characters, assume all characters are numeric
    implicit:

E

D

A
- create a dict map of string int to int
- initialize the sum to 0
- split the integer string into ones, tens, hundreds, thousands, etc places list
- reverse the list
- for idx, item in the list, add the value of the dict map lookup, times 10*index
'''

def string_to_integer(string_number):
    values = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    sum = 0
    places = reversed(list(string_number))
    for idx, num in enumerate(places):
        sum += values[num] * (10**idx)
    return sum

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
