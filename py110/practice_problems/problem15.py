# Create a function that takes a string argument that consists entirely of
# numeric digits and computes the greatest product of four consecutive digits
# in the string. The argument will always have more than 4 digits.

"""
P
input: a string of numeric digits
output: the greatest product of four consecutive digits
rules:
- there will always be more than 4 digits in the input string
- all input string numbers are positive

E

 max ( prod (slice[0:4]) , ...  prod (slice[len-4:len]) )


 '3456' => 3 * 4 * 5 * 6
 '3456' => '3' '4' '5' '6'
 '3' '4' '5' '6' => 3 4 5 6
 3 4 5 6 => 3 * 4 * 5 * 6

D

A
for each slice of 4 consecutive numbers, convert from a string to a product and return the max

"""

from math import prod

def product(integer):
    return prod([int(num) for num in integer])

def greatest_product(string_number):
    consecutive_products = [product(string_number[i:i + 4]) for i in range(len(string_number) - 3)]
    return max(consecutive_products)


# Examples
print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
# The above tests should each print True.
