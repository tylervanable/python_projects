"""
    Calculate how much each person should pay for a meal with friends.
    Consider the cost of the tip and how many people will split the bill.

    This version includes the .format with format specifier. This version
    also includes different variables for tip and tip percentage.

    Tyler
    5/13/24
"""


# Annotate the variables and obtain user inputs.
bill_cost: float = float(input("What was the total bill? "))
tip: int = int(input("How much tip would you like to give? 15, 20, 25? "))
tip_percentage: float = float(tip/100 + 1)
bill_after_tax: float = float(bill_cost*tip_percentage)
num_people: int = int(input("How many people to split the bill? "))
cost_per_person: float

# Calculate the split cost of the bill.
cost_per_person = bill_after_tax / num_people
cost_per_person = float("{:.2f}".format(cost_per_person))

# Display the split cost of the bill.
print(f"Each person should pay: ${cost_per_person}.")
