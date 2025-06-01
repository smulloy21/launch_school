# Comments show expected output
print("Hello")                  # <class 'str'>
print(5)                        # <class 'int'>
print([1, 2, 3])                # <class 'list'>

print(type("Hello").__name__)   # str
print(type(5).__name__)         # int
print(type([1, 2, 3]).__name__) # list
