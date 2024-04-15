"""
    When an object is falling because of gravity, the following formula can be
    used to determine the distance the object falls in a specific time period:
        d = 0.5*g**t

        d is the distance in meters
        g is 9.8
        t is the amount of time in seconds an objects has been falling

    Tyler
    4/15/24
"""


def falling_distance(falling_time: float) -> float:
    """Calculate the falling distance of an object and return it."""

    # Annotate the variable and define the constant.
    GRAVITY: float = 9.8
    
    distance: float

    # Calculate the falling distance of the user's object.
    distance = 0.5*GRAVITY*falling_time**2

    # Return the distance variable.
    return distance

def main() -> None:
    """Obtain the falling time from the user, return that value and
       display the distance to the user after it is calculated in the
       invocation of falling_distance."""

    # Annotate the variables.
    falling_time: float

    # Obtain the falling time from the user.
    falling_time = float(input("What is the falling time in seconds? "))

    # Invoke the falling_distance function.
    calculated_distance = falling_distance(falling_time)

    # Print the calculated distance.
    print("The distance the object fell is: {}".format(calculated_distance))
    
main()
