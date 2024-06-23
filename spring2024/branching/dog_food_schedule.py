"""
    Obtain the current hour from the user in military time.
    Determine if it is morning, afternoon, or evening, 
    and remind the user to feed their pet if it is morning.

    Tyler
    2/24/24
"""


# Annotate the variables and define the constants.
day: str
hour: int

# Obtain the hour number from the user.
hour = int(input("Please input the current hour as a whole number in military time: "))

# Display a message depending of it is morning, afternoon, or evening.
if hour >= 1 and hour < 12:
    print("It's morning, so don't forget to feed your dog!")
elif hour >= 12 and hour < 17:
    print("It's afternoon, you better had fed your dog!")
elif hour >= 17 and hour <= 24:
    print("It's evening, so why don't you pet your dog?")
