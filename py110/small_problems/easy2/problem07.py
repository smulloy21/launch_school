# Write a function that takes two list arguments, each containing a
# list of numbers, and returns a new list that contains the product of
# each pair of numbers from the arguments that have the same index. You
# may assume that the arguments contain the same number of elements.

'''
P
input: two lists, containing a list of numbers
output: a new list that is the product of the numbers at the same index of the two input lists
rules:
    explicit:
        - assume the arguments contain the same number of elements

E

D

A
- list comprehension of the product of the two tuple elements from the zip of both lists
'''

def multiply_list(list1, list2):
    return [el1 * el2 for (el1, el2) in zip(list1, list2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
