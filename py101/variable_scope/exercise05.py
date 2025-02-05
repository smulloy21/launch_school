# What will the following code do? Don't run it until you have tried to answer.

def my_func():
    num = 10

my_func()
print(num)

# line 7 will raise an exception - num is only defined within the local my_func
# function scope - it is not defined where it is called on line 7
