# Some people believe that Fridays that fall on the 13th day of the
# month are unlucky days. Write a function that takes a year as an
# argument and returns the number of Friday the 13ths in that year. You
# may assume that the year is greater than 1752, which is when the
# United Kingdom adopted the modern Gregorian Calendar. You may also
# assume that the same calendar will remain in use for the foreseeable
# future.


from datetime import date


FRIDAY = 4


def friday_the_13ths(year):
    freaky_fridays = 0
    for i in range(1, 13):
        if date(year, i, 13).weekday() == FRIDAY:
            freaky_fridays += 1

    return freaky_fridays


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
