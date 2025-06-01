class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() != other.name.casefold()


val = Cat('Val')
galaxy = Cat('Galaxy')

print(val != galaxy) # True
galaxy.name = 'val'
print(val == galaxy) # True
