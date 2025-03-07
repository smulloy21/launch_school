# Write a function that rotates the last count digits of a number. To
# perform the rotation, move the first of the digits that you want to
# rotate to the end and shift the remaining digits to the left.


'''
P
input: an integer, and a from-the-right index
output: an integer, with the from-the-right index moved to the end of the number

E
rotate_rightmost_digits(735291, 3) == 735912
735291 => 735912

D

A
- transform the integer into a list of strings
- pop the element at the from-the-right index and append it to the end of the list
- transform the list of string digits back to an integer

'''

def rotate_rightmost_digits(integer, right_index):
    list_of_digits = list(str(integer))
    last_element = list_of_digits.pop(-right_index)
    list_of_digits.append(last_element)
    return int(''.join(list_of_digits))


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
