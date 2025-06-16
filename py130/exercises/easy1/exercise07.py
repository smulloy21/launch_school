list_of_lists = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]

flattened = list(elem for sublist in list_of_lists for elem in sublist)
print(flattened) # [1, 2, 3, 'a', 'b', 'c', True, False]
