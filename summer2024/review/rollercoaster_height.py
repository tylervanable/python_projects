"""
    Check if the user is tall enough to ride a rollercoaster.

    Tyler
    5/14/24
"""


# Annotate the variables.
height: int

# Display a message and obtain the height from the user.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Display a message to the user whether or not if they can ride the rollercoaster.
if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Insert a line break.
print("\n")

# Discuss common Python mistake between '=' and '=='.
print("In Python, '=' and '==' look similar and are commonly mistaken, but have completely different uses.")
print("Using '=' denotes assignment. Whatever is to the right of the '=' sign is stored to the variable on the left.")
print("Using '==' denotes an equality check. Checks whether the values on the left and right sides are equal. If so, True is returned.")
print("An example of an equality check might include: 'if yes == yes:' or 'if height == 120'")

# Insert a line break here.
print("\n")


# Discuss comparison operators.
print("Comparison operators include the following: ")
print("Greater than: '>'")
print("Less than: '<'")
print("Greater than or equal to: '>='")
print("Less than or equal to: '<='")
print("Equal to: '=='")
print("Not equal to: '!='")
print("Note: Make sure to distinguish between '=' and '=='.")
print("... '=' will assign a value while '==' checks if two values are True or False")
