# Write a function that takes a positive integer as an argument and
# returns that number with its digits reversed.

'''
P
input: a positive integer
output: that number with its digits reversed

E

D

A
- convert the integer to a string, reverse the string, convert to an integer
'''


def reverse_number(integer):
    return int(str(integer)[::-1])


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
