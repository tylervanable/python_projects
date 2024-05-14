"""
    Calculate how much each person should pay for a meal with friends.
    Consider the cost of the tip and how many people will split the bill.

    Tyler
    5/13/24
"""


# Annotate the variables and obtain user inputs.
bill_cost: float = float(input("What was the total bill? "))
tip_percentage: float = float(input("How much tip would you like to give? 15, 20, 25? "))
bill_after_tax: float = float(bill_cost*tip_percentage)
num_people: int = int(input("How many people to split the bill? "))
cost_per_person: float

# Calculate and round the split cost of the bill.
cost_per_person = bill_after_tax / num_people
cost_per_person = round(cost_per_person, 2)

# Display the split cost of the bill.
print(f"Each person should pay: ${cost_per_person}.")
