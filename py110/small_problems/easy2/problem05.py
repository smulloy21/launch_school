# Write a function that combines two lists passed as arguments and
# returns a new list that contains all elements from both list
# arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, and that they
# have the same number of elements.


'''
P
input: two lists, with an equal number of elements
output: a single list, where the elements are alternating from each input list

E

D

A
- iterate over the first list and append that element from both lists to a new list, repeat.
- return the new list
'''


# def interleave(lis1, list2):
#     output = []
#     for idx in range(len(list1)):
#         output.append(list1[idx])
#         output.append(list2[idx])
#     return output


def interleave(list1, list2):
    output = []
    for item in zip(list1, list2):
        output.extend(item)
    return output


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
