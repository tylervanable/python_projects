"""
    Calculate the cost of a pizza order depending on the pizza size
    and toppings.

    S: $15 (if pepperoni, add $2)
    M: $20 (if pepperoni, add $3)
    L: $25 (if pepperoni, add $3)
    if extra cheese, add $1
"""


# Annotate the variables and obtain information about the size
# and toppings of the user's pizza order.
size: str = input() # What size pizza do you want? S, M, or L
add_pepperoni: str = input() # Do you want pepperoni? Y or N
extra_cheese: str = input() # Do you want extra cheese? Y or N
cost: int

# Display a welcome message to the user.
print("Thank you for choosing Python Pizza Deliveries!")

# Calculate the cost of the pizza based on its size and toppings.
if size == "S":
  cost = 15
  if add_pepperoni == "Y":
    cost += 2
elif size == "M":
  cost = 20
  if add_pepperoni == "Y":
    cost += 3
elif size == "L":
  cost = 25
  if add_pepperoni == "Y":
    cost += 3
if extra_cheese == "Y":
  cost += 1

# Display the total cost to the user.
print(f"Your final bill is: ${cost}.")

