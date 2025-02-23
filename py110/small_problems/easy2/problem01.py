# Write a function that takes a floating point number representing an
# angle between 0 and 360 degrees and returns a string representing
# that angle in degrees, minutes, and seconds. You should use a degree
# symbol (°) to represent degrees, a single quote (') to represent
# minutes, and a double quote (") to represent seconds. There are 60
# minutes in a degree, and 60 seconds in a minute.

# Note: You can use the following constant to represent the degree
# symbol:

DEGREE = "\u00B0"


'''
P
input: a floating point number, representing an angle between 0 and 360 degrees
output: a string representing that angle in degrees, minutes, and seconds
rules:
    explicit:
        - There are 60 minutes in a degree, and 60 seconds in a minute
        - You can use the constant to represent the degree symbol
    implicit:

E
dms(76.73) == "76°43'48\""
76.73 => 76°
.73 * 60 => 43.8 => 43'
.8 * 60 => 48.0 => 48"


D

A
- take the number and integer divide it by 1  to get the degree, save to a variable
- take the remainder of that division, multiply it by 60 and integer divide it
by 1 to get the minutes, save to a variable
- take the remainder of that division, multiply it by 60 to get the seconds
- output a formatted string with the degrees, minutes, and seconds, using 00 instead of 0

'''


def dms(angle):
    degree, leftover = divmod(angle, 1)
    minutes, leftover = divmod(leftover * 60, 1)
    seconds, _ = divmod(leftover * 60, 1)
    return f'{int(degree)}{DEGREE}{int(minutes):02}\'{int(seconds):02}\"'


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
