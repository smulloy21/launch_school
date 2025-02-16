# Given the following data structure, write some code that defines a
# dictionary where the key is the first item in each sublist, and the
# value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# Expected:
# Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# }

my_dict = {sublist[0]: sublist[1] for sublist in lst}
print(my_dict) # {'a': 1, 'b': 'two', 'sea': {'c': 3}, 'D': ['a', 'b', 'c']}
