# You want to multiply all elements of a list by 2. However, the
# function is not returning the expected result. Explain the bug, and
# provide a solution.

def multiply_list(lst):
    for i, item in enumerate(lst):
        lst[i] = item * 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# The bug was that the code was modifying the loop variable, but not
# the list. The variable `item` is a separate reference to the list
# element, and changing that reference doesn't change the list element.
