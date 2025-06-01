class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')

        if name == '':
            raise ValueError('Name cannot be an empty string.')

        self._name = name


linda = Person('Linda')
print(linda.name)                   # Linda

linda.name = 'Lin'
print(linda.name)                   # Lin

linda.name = ''
# ValueError: Name cannot be an empty string.
