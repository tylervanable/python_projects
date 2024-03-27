"""
    Ask the user how many minutes they played a video game
    for 7 days over 4 weeks.
"""


# Annotate the variables
minutes: int
week: int = 1
day: int = 1
hours: int = 0
hours_total: int = 0

# Obtain how many minutes they user played a video game
# every day for four weeks.
for week in range(1, 5):
    for day in range(1, 8):
        hours = int(input("How many minutes did you play video games on day {} of week {}? "
              .format(day, week)))
        hours_total += hours
        day += 1
    week += 1

print("You've played a total of {} minutes the past four weeks!"
      .format(hours_total))
