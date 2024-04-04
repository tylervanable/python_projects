"""
    Write a function that takes a triangle’s base and height as (parameter) input and returns the area.
    The formula for the area of a triangle is 1/2𝑏ℎ. Invoke the function three times with different
    values for base and height and print the result with one value to the right of the decimal. Do not
    interact obtain any inputs from the user, and do not have the area function print to the console (do
    that in your main function). Here is an example of the program running:
        The area of a triangle of base 2 and height 3 is 3.0.
        The area of a triangle of base 5 and height 10 is 25.0.
        The area of a triangle of base 2 and height 5 is 5.0.

    Tyler
    4/3/24
"""


def calculate_area(base: float, height: float) -> float:
    """Calculate the area of three values from the user."""

    # Annotate the variables.
    area: float

    # Calculate the area of the triangle.
    area = 0.5*base*height

    # Return the value of the triangle.
    return area


def main() -> None:
    """Obtain the base and height from the user and invoke the calculate_area function."""

    # Annotate the variables.
    base: float
    height: float

    # Obtain the base and height from the user three times.
    for i in range(1, 4):
        base = float(input("Please input the base of the triangle: "))
        height = float(input("Please input the height of the triangle: "))

        # Invoke the calculate_area function three times and display the value of the area.
        area = calculate_area(base, height)
        print("The value of triangle number {} is {}".format(i, area))
    

main()
