# How do we create a class and an object in Python?

# Write a program that defines a class and creates two objects from that
# class. The class should have at least one instance variable that gets
# initialized by the initializer.

# What class you create doesn't matter, provided it satisfies the above
# requirements.

class Chair:

    def __init__(self, type):
        self.type = type
        print(f'I am a {type} chair.')

rocker = Chair('rocking')
high_char = Chair('high')
