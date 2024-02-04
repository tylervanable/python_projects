"""
Calculuate the total cost of the movie trip.
Tyler
1/31/24
"""
# Define constant.
SALES_TAX: float = 1.07

# Annotate variables.
amount_of_tickets: int
cost_of_tickets: float
concession_bill: float
bill_after_tax:float

# Obtain the number of tickets, cost of tickets and concession bill from the user. 
amount_of_tickets = int(input("Please enter the number of tickets purchased: "))
cost_of_tickets = float(input("Please enter the cost of each ticket: "))
concession_bill = float(input("Please enter the total bill at the concession stand: "))

# Calculate the total cost for going to the movies.
bill_after_tax = amount_of_tickets * cost_of_tickets + concession_bill * SALES_TAX

# Print out the total cost of the trip to the movies to the user.
print("The total cost for the trip to the movies is ${}!".format(bill_after_tax))
