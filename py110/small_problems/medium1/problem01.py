# Write a function that rotates a list by moving the first element to
# the end of the list. Do not modify the original list; return a new
# list instead.

# - If the input is an empty list, return an empty list.
# - If the input is not a list, return None.

# Review the test cases below, then implement the solution accordingly.


'''
P
input: a list
output: a new list, with the original list's first element at the end
rules:
    explicit:
        - if input is an empty list, return an empty list
        - if input is not a list, return None

E

D

A
- if input is not a list, return None
- if input is an empty list, return an empty list
- concatenate a slice of all elements of the list except the first, to a list of just the first element
- return the new list
'''


def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    if len(lst) == 0:
        return []
    return lst[1:] + [lst[0]]


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
