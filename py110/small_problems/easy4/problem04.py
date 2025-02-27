# Given a dictionary, return its keys sorted by the values associated
# with each key.


'''
P
input: a dictionary
output: a list of the dictionary keys, sorted by the values

E

D

A
return a list of dictionary keys, sorted by the values
'''

# def sort_by_value(item):
#     return item[1]


# def order_by_value(my_dict):
#     return [key for key, _ in sorted(my_dict.items(), key=sort_by_value)]


def order_by_value(d):
    return sorted(list(d.keys()), key=d.get)


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
