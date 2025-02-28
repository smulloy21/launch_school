# You have a function that is supposed to reverse a string passed as an
# argument. However, it's not producing the expected output. Explain
# the bug, and provide a solution.

def reverse_string(string):
    output = ''
    for char in string:
        output = char + output

    return output

print(reverse_string("hello"))# == "olleh")
