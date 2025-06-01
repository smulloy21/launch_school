# In the previous question, we had a mix-in called SpeedMixin that contained a
# go_fast method. We add this mix-in to the Car class as shown below:


class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
print(small_car.go_fast())
# I am a super fast Car!

# When we called small_car.go_fast, you may have noticed that the output
# includes the vehicle type. How is this done?


# self.__class__.__name__

# 1. self refers to the object referenced by small_car. In this case, that's a
# Car object.

# 2. self.__class__ returns a reference to the Car class, which is an object
# of the type class.

# 3. Finally, self.__class__.__name__ returns the name of the Car class as a
# string: 'Car'.
