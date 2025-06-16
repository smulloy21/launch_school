from functools import reduce

strings = ['oh', 'hi', 'there']

def concat(a, b):
    return a + ' ' + b

concatenated_string = reduce(concat, strings)
print(concatenated_string) # oh hi there
