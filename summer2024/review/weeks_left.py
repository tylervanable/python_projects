"""
    Calculate and display how many weeks the user has left to live
    if they live to 90 years of age. Utilizes an f-string.

    Tyler
    5/13/24
"""

# Annotate the variables and define the constants.
TOTAL_WEEKS: int = int(90*52)

age: int = int(input("How old are you? "))
weeks_lived: int = int(age*52)
weeks_left: int 

# Calculate the number of weeks left in the user's lifetime.
weeks_left = int(TOTAL_WEEKS-weeks_lived)

# Display the number of weeks left.
print(f"You have {weeks_left} weeks left.")
