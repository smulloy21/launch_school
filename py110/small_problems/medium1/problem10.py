# As we've seen in the last few exercises, the Fibonacci series is a
# computationally simple series, However, the results grow at an
# incredibly rapid rate. For example, the 100th Fibonacci number is
# 354,224,848,179,261,915,075 -- that's enormous, especially
# considering that it takes six iterations just to find the first
# 2-digit Fibonacci number.

# Write a function that calculates and returns the index of the first
# Fibonacci number that has the number of digits specified by the
# argument. The first Fibonacci number has an index of 1. You may
# assume that the argument is always an integer greater than or equal
# to 2.

# Since Python version 3.10.7, conversion of large integers to strings
# with more than 4300 digits raises an error. This means that the last
# test case will raise an error.

# To bypass this limitation, we can use set sys.set_int_max_str_digits
# from the sys module to a new upper limit. First, we import the sys
# module, then we call sys.set_int_max_str_digits with the maximum
# digits desired for string conversion.

# import sys

# sys.set_int_max_str_digits(50_000)


import sys

def find_fibonacci_index_by_length(length):
    sys.set_int_max_str_digits(50_000)
    first = 1
    second = 1
    count = 2

    while len(str(second)) < length:
        first, second = second, first + second
        count += 1

    return count


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)
