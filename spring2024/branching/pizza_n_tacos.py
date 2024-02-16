"""
    Compare two numbers
    Tyler
    2/12/24
"""

# Annotate variables
pizza: int
tacos: int

# Ask the user for input values.
pizza = int(input("How many pizzas did you order: "))
tacos = int(input("How many tacos is everyone getting: "))

if pizza > tacos:
    print("You ordered more pizzas than tacos!")    # must have 1 if, can be alone, can have many
elif tacos > pizza:
    print("You ordered more tacos than pizzas!")    # 0 to as many elifs needed
else:
    print("The number of tacos and pizzas are the same.") # 0-1 else statements.
