"""
    Obtain the year the user was born, calculate their age,
    and report their age.

    Tyler
    1/24/24
"""

# Annotate the variables and constants.
CURRENT_YEAR: int = 2024

birth_year: int
age: int

# Obtain the user's birth year.
birth_year = int(input("Please enter your birth year: "))

# Calculate the user's age this year.
age = CURRENT_YEAR - birth_year

# Report the user's age.
print("You will be", age, "years old this year.")
