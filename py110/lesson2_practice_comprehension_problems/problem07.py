# Given the following data structure return a new list identical in
# structure to the original, but containing only the numbers that are
# multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# The returned list should look like this:
# [[], [3, 12], [9], [15, 18]]


# Try to use a comprehension for this. However, we recommend first
# trying it without comprehensions.

multiples_of_3 = [[item for item in sublist if item % 3 == 0] for sublist in lst]
print(multiples_of_3)
