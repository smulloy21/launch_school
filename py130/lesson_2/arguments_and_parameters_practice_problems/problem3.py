# Create a function named describe_pet that takes one positional argument
# animal_type and one keyword argument name with a default value of an empty
# string. The function should print a description of the pet. The function
# should not accept more than 1 positional argument.

def describe_pet(animal_type, *, name=''):
    if name:
        print(f'{name}, the {animal_type}')
    else:
        print(f'This {animal_type} has no name.')

describe_pet('Hamster', name='Harry') # Harry, the Hamster

describe_pet('Cat', 'Dog', name='Pete')
# TypeError: describe_pet() takes 1 positional argument but 2 positional
# arguments (and 1 keyword-only argument) were given
