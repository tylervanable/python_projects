"""
Obtain the user's pace in seconds for running a mile and 
calculate marathon time in hours using Galloway's Magic Mile formula.

Tyler
1/29/24
"""
# Variable annotations
MARATHON_MULTIPLIER: float = 1.3
MARATHON_IN_MILES: float = 26.2
SECONDS_IN_HOUR: int = 3600

mile_pace: float
marathon_mile_pace: float
Marathon_time_seconds: float
marathon_time_hours: float

# Obtain the user's pace in seconds for running a mile. 
mile_pace = float(input("How many seconds does it take you to run a mile? "))

# Calculate marathon time in hours using Galloway
marathon_mile_pace = float(mile_pace * MARATHON_MULTIPLIER)
marathon_time_seconds = float(marathon_mile_pace * MARATHON_IN_MILES)
marathon_time_hours = float(marathon_time_seconds/SECONDS_IN_HOUR)

# Print marathon time in hours
print("It will take you {} hour(s) to run a marathon".format(marathon_time_hours))
