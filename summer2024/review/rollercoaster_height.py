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
