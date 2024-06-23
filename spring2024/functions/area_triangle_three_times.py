"""
    Calculate the area of a triangle for the user three times.
    Write a function that takes a triangle’s base and height as (parameter) input and returns the area.

    Function calculate_area will calculate the area of a triangle and return to main.
    Function main is where execution begins. Inputs are obtained from the user and the
    calculate_area function is called three times. Three different areas are displayed
    to the user.

    Tyler
    4/3/24
"""


def calculate_area(base: float, height: float) -> float:
    """Calculate the area of a triangle from the user."""

    # Annotate the variable.
    area: float

    # Calculate the area of the triangle.
    area = 0.5*base*height

    # Return the value of the triangle.
    return area


def main() -> None:
    """Obtain the base and height from the user and invoke the calculate_area function three times."""

    # Annotate the variables.
    base: float
    height: float

    # Obtain the base and height from the user three times.
    for i in range(0, 3):
        base = float(input("Please input the base of the triangle: "))
        height = float(input("Please input the height of the triangle: "))

        # Invoke the calculate_area function three times and display the value of the area.
        area = calculate_area(base, height)
        print("The value of triangle number {} is {}".format(i, area))
    
# Invoke the main function to obtain user inputs. 
main()
