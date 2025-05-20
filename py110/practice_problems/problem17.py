# Create a function that takes a list of integers as an argument. The function
# should determine the minimum integer value that can be appended to the list
# so the sum of all the elements equals the closest prime number that is
# greater than the current sum of the numbers. For example, the numbers in
# [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we
# can add 1 to the list to sum to 7.

# Notes:
# - The list will always contain at least 2 integers.
# - All values in the list must be positive (> 0).
# - There may be multiple occurrences of the various numbers in the list.

"""
P
input: a list of integers
output: the minimum integer value that can be appended to the list so the sum of all elements
equals the next closest prime number

E

D

A
- is_prime HELPER takes in an integer and returns T/F whether it is prime
- if numbers from 2 through integer - 1 have non-zero modulos, the number is prime

- set `initial_sum` equal to the sum of the integer list input
- set `min_integer` to 1
- while True,
-- if `initial_sum` + `min_integer` is prime:
--- return `min_integer`
-- else
--- increment `min_integer` by one

"""

def is_prime(integer):
    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True

def nearest_prime_sum(integers):
    initial_sum = sum(integers)
    min_integer = 1
    while True:
        if is_prime(initial_sum + min_integer):
            return min_integer
        min_integer += 1


# Examples
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
# The above tests should each print True.
