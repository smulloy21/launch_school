# Write a function that takes two sorted lists as arguments and returns a new
# list that contains all the elements from both input lists in ascending
# sorted order. You may assume that the lists contain either all integer
# values or all string values.

# You may not provide any solution that requires you to sort the result list.
# You must build the result list one element at a time in the proper order.

# Your solution should not mutate the input lists.

"""
P
input: 2 sorted lists
output: 1 sorted list, with all the elements from the 2 lists
rules:
- do not sort after merging - only merge one element at a time and sort as you go
- do not mutate the input lists

E
[1, 5, 9]
[2, 6, 8] => [1, 2, 5, 6, 8, 9]


D

A
- if either list is empty, return the other list
- initialize an empty list `merged`
- keep 2 counters for what index we're on in each respective list, starting at 0
- while both counters are less than their respective list's length,
-- check the elements in the list at each counter and see which is smaller
-- append the smaller to the `merged` list
-- increase one on the counter for that respective list
-- if this is the last element of its list,
--- append the rest of the other list to the `merged` list
- return the merged list

"""

def merge(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    merged = []
    idx1, idx2 = 0, 0
    while idx1 < len(lst1) and idx2 < len(lst2):
        elem1, elem2 = lst1[idx1], lst2[idx2]
        if elem1 <= elem2:
            merged.append(elem1)
            idx1 += 1
            if idx1 == len(lst1):
                merged.extend(lst2[idx2:])
        else:
            merged.append(elem2)
            idx2 += 1
            if idx2 == len(lst2):
                merged.extend(lst1[idx1:])


    return merged


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
