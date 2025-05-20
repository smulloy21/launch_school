# A triangle is classified as follows:

# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is
# different.
# Scalene: All three sides have different lengths.

# To be a valid triangle, the sum of the lengths of the two shortest
# sides must be greater than the length of the longest side, and every
# side must have a length greater than 0. If either of these conditions
# is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a
# triangle as arguments and returns one of the following four strings
# representing the triangle's classification: 'equilateral',
# 'isosceles', 'scalene', or 'invalid'.

'''
P
input: 3 sides of a potential triangle
output: 'equilateral'/'isosceles'/'scalene'/'invalid' depending on which the triangle is, based on its sides

E

D

A
- determine if the triangle is invalid, return 'invalid'
- determine if the triangle is equilateral, return 'equilateral'
- determine if the triangle is isosceles, return 'isosceles'
- return 'scalene'

'''


def triangle(side1, side2, side3):
    if 0 in [side1, side2, side3] or (
        side1 + side2 < side3 or
        side2 + side3 < side1 or
        side1 + side3 < side2
    ):
        return 'invalid'
    if side1 == side2 == side3:
        return 'equilateral'
    if (side1 == side2 or
        side2 == side3 or
        side3 == side1
    ):
        return 'isosceles'

    return 'scalene'


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
