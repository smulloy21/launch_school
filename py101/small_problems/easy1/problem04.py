# Build a program that asks the user to enter the length and width of a
# room, in meters, then prints the room's area in both square meters
# and square feet.

# Note: 1 square meter == 10.7639 square feet

length = float(input('What is the length of the room (in meters?) '))
width = float(input('What is the width of the room (in meters)? '))
square_meters = length * width
square_feet = square_meters * 10.7639

print(f'The room is {square_meters} square meters, or {square_feet} square feet.')
