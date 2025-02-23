# Write a function that counts the number of occurrences of each
# element in a given list. Once counted, print each element alongside
# the number of occurrences. Consider the words case sensitive e.g.
# ("suv" != "SUV").

'''
P
input: a list of strings
output: a print of each unique element of the list along with the count of how many times
it appeared in the list

E

D

A
- coerse the list to a set
- for each item in the set, print it + '=>' + its count in the original list
'''


def count_occurrences(lst):
    for element in set(lst):
        print(f'{element} => {lst.count(element)}')


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Expected output:
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2
