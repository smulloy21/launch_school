class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

    def get_wheels(self):
        pass


class Car(Vehicle):
    def get_wheels(self):
        return 4


class Motorcycle(Vehicle):
    def get_wheels(self):
        return 2


class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6
