def reduce(callback, iterable, initial_value):
    accum = initial_value
    for item in iterable:
        accum = callback(item, accum)
    return accum

# Use the reduce function shown in the answer to the previous question to
# compute the sum of the squares in a list of numbers.

numbers = (1, 2, 3, 4)
sum_of_squares = lambda number, accum: accum + number**2
print(reduce(sum_of_squares, numbers, 0)) # 30
