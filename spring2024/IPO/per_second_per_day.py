"""
Convert per-second rate to a per-day rate and report calculations to user.
Tyler
2/5/24
"""

# Define the constant.
SECONDS_IN_DAY: int = 86400

# Annotate the variables.
per_second_rate: int
day_rate: int

# Obtain the user's per-second rate.
per_second_rate = int(input("Please enter the per-second rate: "))

# Calculate the user's per-day rate given the per-second rate.
day_rate = per_second_rate*SECONDS_IN_DAY

# Display the user's conversion of per-second rate to per-day rate.
print("The rate of {:d} per second is equivalent to {:d} per day."
      .format(per_second_rate,day_rate))
