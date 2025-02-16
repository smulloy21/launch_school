# Given the following data structure, write some code to return a list
# that contains only the dictionaries where all the numbers are even.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Expected:
# [{e: [8], f: [6, 10]}]

def all_even(lst_of_lsts):
    for sublist in lst_of_lsts:
        if not all([item % 2 == 0 for item in sublist]):
            return False
    return True

only_even = [dictionary for dictionary in lst if all_even(dictionary.values())]
print(only_even)
