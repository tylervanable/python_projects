"""
    Write a program that will calculate an area for the user.
    The program should begin by presenting the user with a menu
    of different shapes. (e.g., it could present square, circle,
    rectangle, and triangle.) It should prompt the user to make
    a selection from the menu.
    Depending on the choice, it will then prompt the user for
    the dimensions needed to compute the area, it will compute
    the area, and report the area to the user. You can use the
    following area formulae:

    Area of a square = side**2
    Area of a rectangle = width * height
    Area of a triangle = 0.5*base*height
    Area of a circle = pi * radius**2

    Tyler
    4/19/24
"""


import math

def calc_square_area(side: float) -> float:
    """Calculate the area of a square given its side."""

    # Annotate the variable.
    side: float

    # Calculate the area of the square.
    area = side**2
    
    # Return the area of the square
    return area

def calc_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""

    # Annotate the variables.
    width: float
    height: float

    # Calculate the area of the rectangle.
    area = width*height

    # Return the area of the rectangle.
    return area

def calc_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle given its base and height."""

    # Annotate the variables.
    base: float
    height: float

    # Calculate the area of the triangle.
    area = 0.5*base*height

    # Return the area of the triangle.
    return area

def calc_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius."""

    # Annotate the variables.
    radius: float

    # Calculate the area of the circle.
    area = math.pi * radius**2

    # Return the area of the circle.
    return area

def main() -> None:
    """Display a menu of different shapes to the suer and obtain which
       shape the user wants to calculate the area. Later display the
       area to the user."""

    # Annotate the variables.
    side: float
    width: float
    height: float
    base: float
    radius: float
    shape_choice: int

    # Display a menu of shapes to the user.
    print("1. Calculate the area of a square.")
    print("2. Calculate the area of a rectange.")
    print("3. Calculate the area of a triangle.")
    print("4. Calculate the area of a circle.")
    shape_choice = int(input("Please enter 1, 2, 3, or 4 to select a shape: "))

    # Branch into the user's shape choice, collect their shape dimensions, and invoke the function.
    if shape_choice == 1:
        side = float(input("Enter the value of the side of your square: "))
        area = calc_square_area(side)
        
    elif shape_choice == 2:
        width = float(input("Enter the value of the width of your rectangle: "))
        height = float(input("Enter the value of the height of your rectangle: "))
        area = calc_rectangle_area(width,height)
        
    elif shape_choice == 3:
        height = float(input("Enter the value of the height of your triangle: "))
        base = float(input("Enter the value of the base of your triangle: "))
        area = calc_triangle_area(height,base)
        
    elif shape_choice == 4:
        radius = float(input("Enter the value of the radius of your circle: "))
        area = calc_circle_area(radius)

    # Display the area of the user's shape to the user.
    print("The area of your shape is {:.2f}".format(area))

main()
