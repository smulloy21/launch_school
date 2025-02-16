# Given the following data structure, write some code to return a list
# that contains the colors of the fruits and the sizes of the
# vegetables. The sizes should be uppercase, and the colors should be
# capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# The return value should look like this:
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

def color_or_size(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    elif item['type'] == 'vegetable':
        return item['size'].upper()

output = [color_or_size(produce) for produce in dict1.values()]
print(output)
