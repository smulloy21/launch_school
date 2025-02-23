# Write a function that takes one argument, a positive integer, and
# returns a list of the digits in the number.

'''
P
input: a positive integer
output: a list of the digits of that number

E
digit_list(12345) == [1, 2, 3, 4, 5]

D

A
list comprehension of the int version of each digit in the string version of the number
'''


def digit_list(integer):
    return [int(num) for num in str(integer)]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
