"""
    Check if the user is tall enough to ride a rollercoaster.
    Utilizes a nested loop and elif statements.

    Tyler
    5/14/24
"""


# Annotate the variables.
height: int
age: int

# Display a message and obtain the height from the user.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Display a message to the user whether or not if they can ride the rollercoaster.
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
