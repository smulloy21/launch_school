class Vehicle:

    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.vehicle_count


class SignalMixin:

    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')


class Car(SignalMixin, Vehicle):
    pass


class Truck(SignalMixin, Vehicle):
    pass


class Boat(Vehicle):
    pass


print(Car.mro())
# [
#   <class '__main__.Car'>,
#   <class '__main__.SignalMixin'>,
#   <class '__main__.Vehicle'>,
#   <class 'object'>
# ]

print(Truck.mro())
# [
#   <class '__main__.Truck'>,
#   <class '__main__.SignalMixin'>,
#   <class '__main__.Vehicle'>,
#   <class 'object'>
# ]

print(Boat.mro())
# [
#   <class '__main__.Boat'>,
#   <class '__main__.Vehicle'>,
#   <class 'object'>
# ]

print(Vehicle.mro())
# [
#   <class '__main__.Vehicle'>,
#   <class 'object'>
# ]
