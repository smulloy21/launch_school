# Which of the following classes would create objects that have an instance
# variable. How do you know?


class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

# the class Pizza would create objects that have the instance variable `my_name`
# Fruit fails to use `self` which is what makes a variable an instance variable

print(vars(Fruit('orange')))     # {}
print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}
