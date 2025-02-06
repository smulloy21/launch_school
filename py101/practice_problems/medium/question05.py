# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan")) # False

# False. Python doesn't let you use == to determine whether a value is nan.

# How can you reliably test if a value is nan?

# you can use math.isnan()

import math

nan_value = float("nan")

print(math.isnan(nan_value)) # True
