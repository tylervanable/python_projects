"""
    Example of a SERIES IF program:
    Obtain the user's favorite member from the Beatles.
    Display a message depending on the user's input. 
    Include Paul, Ringo, John, George, Pete, Stu.

    Tyler
    2/19/24
"""

# Annotate the variables.
favorite_beatle: str

# Obtain the user's favorite Beatle.
favorite_beatle = input("Who is your favorite member of the Beatles?\n(enter their first name only:) ").upper()

# Print a message to the user based on their favorite member of the Beatles.
if favorite_beatle == "PAUL":
    print("Sir Paul is the best")
elif favorite_beatle == "RINGO":
    print("Ringo has the best personality.")
elif favorite_beatle == "JOHN":
    print("John died too young")
elif favorite_beatle == "GEORGE":
    print("George was a great guitarist.")
elif favorite_beatle == "PETE" or favorite_beatle == "STU":
    print("I don't know that Beatle member...")
else:
    print(f"I'm not sure I know {favorite_beatle}...")
