# The time of day can be represented as the number of minutes before or
# after midnight. If the number of minutes is positive, the time is
# after midnight. If the number of minutes is negative, the time is
# before midnight.

# Write a function that takes a time using this minute-based format and
# returns the time of day in 24-hour format (hh:mm). Your function
# should work with any integer input.

# You may not use Python's datetime module.

# Disregard Daylight Savings and Standard Time and other complications.

'''
P
input: a negative or positive integer of a number of minutes before or after midnight
output: a string representing the time of day in 24-hr format (hh:mm)

E

D

A
- first, get the remainder of the given integer % minutes in a day, so we're working with
only one day
- then divide the integer by the number of minutes in an hour - the quotient is the hours
and the remainder is the minutes
- format hours and minutes into the correct string formatting
'''
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR


def time_of_day(delta_minutes):
    delta_minutes %= MINUTES_PER_DAY
    hours, minutes = divmod(delta_minutes, MINUTES_PER_HOUR)
    return f'{hours:02d}:{minutes:02d}'


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
