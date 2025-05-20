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

    def spray_paint(self, color):
        self.color = color
        print(f'Spray painting the car {self.color}.')

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

    @classmethod
    def gas_mileage(cls, miles, gallons):
        mileage = miles / gallons
        print(f'{mileage} miles per gallon')


Car.gas_mileage(351, 13)
# 27.0 miles per gallon
