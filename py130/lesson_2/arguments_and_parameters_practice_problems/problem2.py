# Define a function named multiply that accepts two positional-only arguments
# and returns their product. The function should not allow these parameters to
# be passed as keyword arguments.

def multiply(a, b, /):
    return a * b

print(multiply(3,3)) # 9

multiply(a=3, b=4) # TypeError
