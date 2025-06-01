class WalkingMixin:
    def walk(self):
        return f'{self} {self.gait()} forward'


class Person(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

    def __str__(self):
        return self.name


class Cat(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

    def __str__(self):
        return self.name


class Cheetah(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

    def __str__(self):
        return self.name

class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title

    def gait(self):
        return "struts"

    def __str__(self):
        return f'{self.title} {self.name}'


byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"
