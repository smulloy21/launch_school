# Create a Car class that has a class variable named manufacturer and an
# instance variable named manufacturer. Initialize these variables to
# different values. Add a show_manufacturer method that prints both the class
# and instance variables.


class Car:
    manufacturer = 'Toyota'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f'{self.__class__.manufacturer=}')
        print(f'{self.manufacturer=}')


subu = Car('Subaru')
subu.show_manufacturer()
