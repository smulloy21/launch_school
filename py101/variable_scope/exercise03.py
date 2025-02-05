# What will the following code print and why? Don't run it until you
# have tried to answer.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)
# this will print 10. the global keyword in my_func affects the value
# for the global variable num, changing it to 10
