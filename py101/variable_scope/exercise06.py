# What will the following code print and why? Don't run it until you
# have tried to answer.

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# this will print "Inner 1: 25\nInner2: 15". in inner_func1, a local x variable
# is assigned the value 25, whereas in inner_func2, the x variable is found by
# looking within the outer scope, namely, my_func, where it has the value 15
