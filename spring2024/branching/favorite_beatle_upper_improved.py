"""
    Improve the favorite member from the Beatles program with use of .upper()
    to ignore capitalization mistakes in the user's input.

    Tyler
    2/19/24
"""

# Annotate the variables.
favorite_beatle: str

# Obtain the user's favorite Beatle.
favorite_beatle = input("Who is your favorite member of the Beatles?\n(enter their first name only):\n")

# Print a message to the user based on their favorite member of the Beatles.
if favorite_beatle.upper() == "PAUL":
    print("Sir Paul is the best")
elif favorite_beatle.upper() == "RINGO":
    print("Ringo has the best personality.")
elif favorite_beatle.upper() == "JOHN":
    print("John died too young")
elif favorite_beatle.upper() == "GEORGE":
    print("George was a great guitarist.")
elif favorite_beatle.upper() == "PETE" or favorite_beatle == "STU":
    print("I don't know that Beatle member...")
else:
    print(f"I'm not sure I know {favorite_beatle}...")
