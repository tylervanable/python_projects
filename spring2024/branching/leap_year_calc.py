"""
    Determine whether a user-given year is a leap year.
    Rules:
    Every year divisible by four is a leap year.
    But years divisible by 100 are not a leap year.
    THO years divisible by 400 ARE a leap year (eg 1600, 2000)

    Tyler
    2/25/24
"""

# Annotate the variables.
year: int
leapYear: bool

# Obtain the year from the user and determine whether
# a user-given year a leap year (is divisible by 4, 100, and 400).
year = int(input("Please input a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year {} is a leap year!"
                  .format(year))
        else:
            print("The year {} is NOT a leap year!"
                  .format(year))
    else:
        print("The year {} is a leap year!"
              .format(year))
else:
    print("The year {} is NOT a leap year!"
          .format(year))

