# Which of the following are objects in Python? If they are objects, how can
# you find out what class they belong to?

print(True.__class__)
print('hello'.__class__)
print([1, 2, 3, 'happy days'].__class__)
print((142).__class__)
print({1, 2, 3}.__class__)
print(1.2345.__class__)

# These are all objects in Python, and you can find out what class the belong to
# by calling .__class__ on them
