# Write two different ways to remove all of the elements from the following list:

numbers = [1, 2, 3, 4]

numbers.clear()
while numbers:
    numbers.pop()

print(numbers) # []
