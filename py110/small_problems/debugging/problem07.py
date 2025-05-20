# We defined a function intending to multiply the sum of numbers by a
# factor. However, the function raises an error. Why? How would you fix
# this code?

def sum_with_factor(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_with_factor(numbers, 2) == 20)


# The problem is the code is overwriting the sum() function in the
# local namespace. The best way to fix is to use a different function
# name for our new sum function
