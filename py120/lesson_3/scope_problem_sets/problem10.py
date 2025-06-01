class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?

# Without running the above code, what will it output? If it raises an error,
# explain why and how to fix it.

# Raises an AttributeError cause species is never initialized as an instance variable.
# To fix, need to `super().__init__(species)` in the Sparrow `__init__` method
