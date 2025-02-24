# As seen in the previous exercise, the time of day can be represented
# as the number of minutes before or after midnight. If the number of
# minutes is positive, the time is after midnight. If the number of
# minutes is negative, the time is before midnight.

# Write two functions that each take a time of day in 24 hour format,
# and return the number of minutes before and after midnight,
# respectively. Both functions should return a value in the range 0
# through 1439.

# You may not use Python's datetime module.

'''
P
input: a string representing time on a 24 hr clock (hh:mm)
output: an integer representing how many minutes before or after midnight the time is

E

D

A
- take the string, split it at the colon and coerse both hours and minutes to ints
- in after_midnight, add the hours integer * 60 to the minutes integer and return the result %
minutes per day
- in before_midnight, take hours in a day and subtract the hours and minutes from it to get the
difference, return the result % minutes per day
'''
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR


def after_midnight(time_string):
    hours, minutes = time_string.split(':')
    return (int(hours) * MINUTES_PER_HOUR + int(minutes)) % MINUTES_PER_DAY


def before_midnight(time_string):
    return (MINUTES_PER_DAY - after_midnight(time_string)) % MINUTES_PER_DAY


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# Disregard Daylight Savings and Standard Time and other irregularities.
