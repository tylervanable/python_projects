"""
    Calculate's the user's CD interest rate given their tax bracket 
    (as decimal) and interest rate (as percent). 

    Tyler
    2/5/24
"""

# Define the constant.
TAX_BRACKET_CONSTANT: int = 1

# Annotate the variables.
tax_bracket: float
interest_rate: float
cd_interest_rate: float

# Request user's tax bracket (as decimal) and municipal bond interest rate (as %)
tax_bracket = float(input("Enter the tax bracket (as decimal): "))
interest_rate = float(input("Enter municipal bond interest rate (as %): "))

# Calculate the user's CD interest rate.
cd_interest_rate = interest_rate/(TAX_BRACKET_CONSTANT-tax_bracket)

# Report the calculated CD interest rate to the user.
print("Equivalent CD interest rate: {:.3f}%".format(cd_interest_rate))
