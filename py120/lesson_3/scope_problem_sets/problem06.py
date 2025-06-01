class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

timmy = Student('timmy')
jane = Student('jane')

print(timmy.name)
print(timmy.__class__.school_name)
print(jane.name)
print(jane.__class__.school_name)
