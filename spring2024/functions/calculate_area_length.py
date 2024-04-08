"""
    Obtain the length and wwidth of a rectangle from the user.
    Invoke the calculate_area and calculate_perimeter functions.

    area of a rectangle = length x width
    perimeter of a rectangle = 2 x (length + width)

    Notes:
    formal parameter (looks like annotation inside argument function def)
    actual parameter (a variable or variables argument inside the function call)
    
    Tyler
    Happy April Fool's Day!
"""


def calculate_area(length: float, width: float):
    """Calculate and display the area of the rectangle
    with dimensions length and width."""

    # Annotate the variable.
    area: float

    # Calculate the area of the rectangle.
    area = length * width

    # Display the area of the rectangle to the user.
    print("The area of the rectangle is {}.".format(area))

def calculate_perimeter(length: float, width: float):
    """Calculate and display the perimeter of the rectangle
    with dimensions length and width."""

    # Annotate the variable.
    perimeter: float

    # Calculate the perimeter of the rectangle.
    perimeter = 2 * (length + width)

    # Display the perimeter of the rectangle to the user.
    print("The perimeter of the rectangle is {}.".format(perimeter))


def main():
    """Obtain the length and width of a rectangle and then
    invoke calculate_area and calculate_perimeter to calculate
    and display the area and the perimeter."""

    # Annotate the variables.
    length: float
    width: float

   # Obtain the length and the width from the user.
    length = float(input("What is the rectangle's length? "))
    width = float(input("What is the rectangle's width? "))

    # Calculate and display the area and perimeter.
    calculate_area(length, width)
    calculate_perimeter(length, width)

main()
