# Write a function that takes a list of numbers and returns the inverse of
# each number (if n is a number, then 1 / n is its inverse). Handle any
# exceptions that might occur.

def invert(lst):
    output = []
    for num in lst:
        try:
            output.append(1/num)
        except ZeroDivisionError:
            output.append(float('inf'))

    return output

numbers = [1, 2, 0, 3, 4]
print(invert(numbers))
