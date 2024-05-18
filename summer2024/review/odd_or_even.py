"""
    Check and print whether a number is odd or even.

    Tyler
    5/17/24
"""


# Annotate the variable and obtain a number from the user.
number: int = int(input("Enter a number: "))

# Calculate and display whether the user's number is an even or odd number.
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
