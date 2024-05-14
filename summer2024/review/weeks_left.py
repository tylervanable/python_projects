"""
    Calculate and display how many weeks the user has left to live
    if they live to 90 years of age. Utilizes an f-string.

    Tyler
    5/13/24
"""

# Annotate the variables.
age: int = int(input("How old are you? "))
years_left: int = 90-int(age)
weeks_left: int 

# Calculate the number of weeks left in the user's lifetime.
weeks_left = int(years_left*52)

# Display the number of weeks left.
print(f"You have {weeks_left} weeks left.")
