lst = [1, 2, None, 3, 4, None, 5]

no_nones = list(filter(lambda elem: elem is not None, lst))
print(no_nones) # [1, 2, 3, 4, 5]
