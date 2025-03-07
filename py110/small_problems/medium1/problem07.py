# The Fibonacci series is a sequence of numbers in which each number is
# the sum of the previous two numbers. The first two Fibonacci numbers
# are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3,
# the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In
# mathematical terms, this can be represented as:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

# Write a function called fibonacci that computes the nth Fibonacci
# number, where nth is an argument passed to the function:

# If you're familiar with the concept of recursive functions, don't try
# to write a recursive solution at this time; you'll do that in the
# next exercise. In other words, write a procedural function that
# doesn't try to call itself.

# If you don't know about or understand recursion, don't worry about
# it. You'll learn soon enough.


'''
P
input: a positive integer, n
output: the nth fibonacci number
rules:
    - do not use recursion to solve

E

D

A
- guard clause to handle cases 1 and 2
- create two variables, for the previous two fibonacci numbers, initialized to 1
- for num in range(3, integer):
- add the two variables together for the current numth fibonacci number
- the


'''

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    minus_2 = 1
    minus_1 = 1
    for _ in range(3, n + 1):
        current = minus_2 + minus_1
        minus_2, minus_1 = minus_1, current
    return current


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
