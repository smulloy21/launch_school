# Take the number 735291 and rotate it by one digit to the left,
# getting 352917. Next, keep the first digit fixed in place and rotate
# the remaining digits to get 329175. Keep the first two digits fixed
# in place and rotate again to get 321759. Keep the first three digits
# fixed in place and rotate again to get 321597. Finally, keep the
# first four digits fixed in place and rotate the final two digits to
# get 321579. The resulting number is called the maximum rotation of
# the original number.

# Write a function that takes an integer as an argument and returns the
# maximum rotation of that integer. You can (and probably should) use
# the rotate_rightmost_digits function from the previous exercise.


'''
P
input: an integer
output: an integer, that is the 'maximum rotation' of the original number

E
735291 => 352917 (rotate_rightmost_digits(int, -len(int))
352917 => 329175 (rotate_rightmost_digits(int, -(len(int)-1)))
...
321597 => 321579 (rotate_rightmost_digits(int, -1))

D

A
- for X in range in len(int), 1, -1:
-- int = rotate_rightmost_digits(int, X)
- return int
'''

def max_rotation(integer):
    for i in range(len(str(integer)), 1, -1):
        integer = rotate_rightmost_digits(integer, i)
    return integer

def rotate_rightmost_digits(integer, right_index):
    list_of_digits = list(str(integer))
    last_element = list_of_digits.pop(-right_index)
    list_of_digits.append(last_element)
    return int(''.join(list_of_digits))

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
