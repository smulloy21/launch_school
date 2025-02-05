# What will the following code print and why? Don't run it until you
# have tried to answer.

num = 5

def my_func():
    num = 10

my_func()
print(num)
# this will print 5. my_func variable shadows num, but never prints it.
# on line 10, the global variable num is unchanged and prints as 5
