# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product
# of all numbers between 1 and the entered integer, inclusive.

# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

import math


num = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, '
                  'or "p" to compute the product. ')
print()

if operation == "s":
    sum = sum(range(1, num+1))
    print(f'The sum of the integers between 1 and {num} is {sum}.')
elif operation == "p":
    product = math.prod(range(1, num+1))
    print(f'The product of the integers between 1 and {num} is {product}.')
else:
    print('Invalid operation.')
