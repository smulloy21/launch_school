# Write a function that takes one argument, a positive integer, and
# returns the sum of its digits.


'''
P
input: a positive integer
output: the sum of its digits

E
sum_digits(23) == 5
23 => [2, 3]
sum([2, 3])

D

A

'''


def sum_digits(integer):
    digits = [int(digit) for digit in str(integer)]
    return sum(digits)


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
