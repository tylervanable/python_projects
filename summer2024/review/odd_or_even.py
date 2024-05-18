"""
    Check and print whether a number is odd or even.

    Tyler
    5/17/24
"""


# Annotate the variables and obtain a number from the user.
number: int = int(input("Enter a number: "))
remainder: int

# Calculate the remainder of the user's number when dividing by 2.
remainder = number % 2

# Display whether the user's number is an even or odd number.
if remainder == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
