# Suppose you have the following class:

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count


# Explain what the _cats_count variable is, what it does in this class, and
# how it works. Write some code to test your theory.


# _cats_count is a class variable counter that gets incremented at the
# initialization of each new Cat object

cosmo = Cat('russian blue')
print(Cat.cats_count()) # 1

galaxy = Cat('tabby')
print(Cat.cats_count()) # 2
