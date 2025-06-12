# Create a generator expression that generates the reciprocals of the numbers
# from 1 to 10. A reciprocal of a number n is 1 / n. Use a for loop to print
# each value.

reciprocols = (1 / n for n in range(1, 11))

for value in reciprocols:
    print(value)
