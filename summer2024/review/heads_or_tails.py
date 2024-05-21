"""
    Generate either a 0 or 1 using the random library.
    Display either tails if the whole number is 0 or
    heads if 1.
"""


# Annotate the variables.
whole_number: int
coin_flip: str

# Import the random module.
import random

# Generate a random whole number, either 0 and 1.
whole_number = random.randint(0, 1)

# Assign the coin_flip variable as Tails if 0 and Heads if 1.
if whole_number == 0:
  coin_flip = "Tails"
else:
  coin_flip = "Heads"

# Display the coin flip result.
print("Flipping a coin...")
print(coin_flip)

