# Write a function that takes two arguments, a string and a positive
# integer, then prints the string as many times as the integer indicates.

def repeat(string, number):
    for _ in range(number):
        print(string)

repeat('Hello', 3)
# Hello
# Hello
# Hello
