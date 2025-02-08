# Given the following similar sets of code, what will each code snippet print?

# A)
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one is: ["one"]
print(f"two is: {two}") # two is: ["two"]
print(f"three is: {three}") # three is: ["three"]

# B)
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one is: ["one"]
print(f"two is: {two}") # two is: ["two"]
print(f"three is: {three}") # three is: ["three"]

# C)
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one is: ["two"]
print(f"two is: {two}") # two is: ["three"]
print(f"three is: {three}") # three is: ["one"]


# In the C case, the mess_with_vars function modifies the content of
# the lists directly. Since lists in Python are mutable and passed by
# object reference, the changes are reflected outside the function.
