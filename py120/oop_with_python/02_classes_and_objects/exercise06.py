class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    # @staticmethod
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


tonka = Car('Jeep', 2018, 'blue')
tonka.get_speed()
tonka.engine_on()
tonka.get_speed()
tonka.accelerate()
tonka.get_speed()
tonka.brake()
tonka.get_speed()
tonka.engine_off()
