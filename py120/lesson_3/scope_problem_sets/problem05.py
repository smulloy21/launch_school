# Define a Student class that has a class variable named school_name. You
# should initialize the school name to 'Oxford'. After defining the class,
# instantiate an instance of the Student class and print the school name using
# that instance.

class Student:
    school_name = 'Oxford'


timmy = Student()
print(timmy.school_name) # Oxford
print(timmy.__class__.school_name) # Oxford
