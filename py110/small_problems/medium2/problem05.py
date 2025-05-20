# A featured number (something unique to this exercise) is an odd
# number that is a multiple of 7, with all of its digits occurring
# exactly once each. For example, 49 is a featured number, but 98 is
# not (it is not odd), 97 is not (it is not a multiple of 7), and 133
# is not (the digit 3 appears twice).

# Write a function that takes an integer as an argument and returns the
# next featured number greater than the integer. Issue an error message
# if there is no next featured number.

# NOTE: The largest possible featured number is 9876543201.

"""
P
input: an integer
output: an integer representing the next-highest featured number
rules:
    - a featured number is odd, a multiple of 7, and all its digits occur once
    - 9876543201 is the largest possible featured number
    - return an error message if there is no next featured number

E

D
- a range

A
- starting from the input number, count up until we find a successful featured number, and return it

- if the input number is equal or greater than the max featured number, return the error message.

- HELPER `is_featured` - returns true if an integer is a featured number, i.e. it:
-- is odd
-- is a multiple of 7
-- has each digit appear only once

- starting from the input number, count up until we find a featured number (using the `is_featured` HELPER) and return it

"""
MAX_FEATURED = 9876543201

def all_unique_digits(num):
    return len(set(str(num))) == len(str(num))

def next_featured(num):
    if num >= MAX_FEATURED:
        return 'There is no possible number that fulfills those requirements.'

    next_seven = num + (7 - num % 7)
    if next_seven % 2 == 0:
        next_seven += 7

    for i in range(next_seven, MAX_FEATURED + 1, 14):
        if all_unique_digits(i):
            return i


print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
