# Write a function that takes a list as an argument and returns a list
# that contains two elements, both of which are lists. Put the first
# half of the original list elements in the first element of the return
# value and put the second half in the second element. If the original
# list contains an odd number of elements, place the middle element in
# the first half list.

'''
P
input: a list containing zero or more elements
output: a list of two lists, the first containing the first half(+) of the original list, the
second containing the second half
rules:
    explicit:
        - if there are an odd number of elements, the middle element should be in the first list
        -
    implicit:
        - an empty list should return two empty lists
        - a list with one element should return a list with that element, and an empty list

E

D

A
- find the middle index by dividing the length of the list by 2
- if length is odd, be sure to include the middle index in the first list
- the first list is a slice from the beginning of the list to the middle index, inclusive if odd
- the second list is a slice from the middle index to the end of the list
- return both new lists

'''


def halvsies(lst):
    middle_index = len(lst) // 2
    if len(lst) % 2 != 0:
        first_list = lst[:middle_index + 1]
        second_list = lst[middle_index + 1:]
    else:
        first_list = lst[:middle_index]
        second_list = lst[middle_index:]
    return [first_list, second_list]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
