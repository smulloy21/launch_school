# What will the following code print and why? Don't run it until you
# have tried to answer.

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# this will print "Hello World" - the inner function has access to the
# outer function's scope, including the outer_var variable
