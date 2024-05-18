"""
    Determine if a user-given year is a leap year and display if it is
    or is not a leap year to the user.

    Leap year rules:
    Every four years is a leap year
    Except every 100 years
    However it IS a leap year every 400 years.

    Tyler
    5/18/24
"""

# Annotate the variable and obtain a year from the user.
year: int = int(input())

# Check if the year is a leap year and display if it is a leap
# year to the user.
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
