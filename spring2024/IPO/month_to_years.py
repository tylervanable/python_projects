"""
    Convert a whole number of months into years and months.
    Display years and months

    Tyler
    2/5/24
"""


# Define the constant.
MONTHS_IN_YEAR: int = 12

# Annotate the variable
total_months: int
years: int
remainder_months: int

# Obtain the user's amount of months.
total_months = int(input("Enter the number of months: "))

# Convert the number of months to years and months.
years = total_months//MONTHS_IN_YEAR
remainder_months = total_months%MONTHS_IN_YEAR

# Display the number of years and months to the user.
print("{} months is {} years and {} months.".format(total_months,years,remainder_months))
