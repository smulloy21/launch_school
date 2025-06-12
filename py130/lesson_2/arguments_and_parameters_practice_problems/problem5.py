# Create a function named find_person that accepts any number of keyword
# arguments in which each key is someone's name and the value is their
# associated profession. The function should check whether any of the
# key/value pairs has a key of "Antonina" and then, if the key is found, print
# a message that shows Antonina's profession. Otherwise, it should say
# "Antonina not found". The function should not accept any positional
# arguments.

def find_person(**kwargs):
    if "Antonina" in kwargs:
        print(f"Antonina's profession is {kwargs['Antonina']}.")
    else:
        print("Antonina not found.")


find_person(John="Engineer", Antonina="Software Engineer")
# Antonina's profession is Software Engineer.

find_person(John="Engineer", Ginni="Software Engineer")
# Antonina not found.
