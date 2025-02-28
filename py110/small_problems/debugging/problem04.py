# You have a function that should check whether a key exists in a
# dictionary and returns its value. However, it's raising an error. Why
# is that? How would you fix this code?

def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))

# Directly addressing a dict key that doesn't exist raises a KeyError.
# The best way to access a dict key when unsure if it exists is to use
# the .get() method, which returns None if the key is not found.
