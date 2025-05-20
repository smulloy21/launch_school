class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def engine_on(self):
        print('Turning the engine on!')

    def accelerate(self):
        print('Accelerating!')
        self.speed += 10

    def brake(self):
        print('Braking!')
        self.speed -= 10

    def engine_off(self):
        self.speed = 0
        print('Turing the engine off!')

    def get_speed(self):
        print(f'Current speed is {self.speed}.')


tonka = Car('Jeep Wrangler', 2018, 'blue')
print(f'My car is {tonka.color}.')
# My car is blue.

print(f"My car's model is a {tonka.model}.")
# My car's model is a Jeep Wrangler.

print(f"My car's year is {tonka.year}.")
# My car's year is 1997.

tonka.color = 'brown'
print(f'My car is now {tonka.color}.')
# My car is now brown.

tonka.year = 2023
# AttributeError: property 'year' of 'Car' object
# has no setter
