# Write a function that takes two lists as arguments and returns a set
# that contains the union of the values from the two lists. You may
# assume that both arguments will always be lists.

'''
P
input: two lists
output: set of the union of the values from the two lists


E

D

A
add the contents of both lists to a set, and return the set
'''


def union(list1, list2):
    my_set = set(list1)
    my_set.update(list2)
    return my_set


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
