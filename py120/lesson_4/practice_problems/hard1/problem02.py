class Vehicle:
    def __init__(self,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicleMixin:
    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicleMixin, Vehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__(50, 25.0)
        self.tires = [30, 30, 32, 32]

class Motorcycle(WheeledVehicleMixin, Vehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__(80, 8.0)
        self.tires = [20, 20]

class Watercraft(Vehicle):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.propellers = number_propellers
        self.hulls = number_hulls

class Motorboat(Watercraft):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)

class Catamaran(Watercraft):
    pass


auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0
