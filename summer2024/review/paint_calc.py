"""
    Calculate the number of cans needed to paint a wall given a height,
    width, and coverage.

    Tyler
    6/7/24
"""


# Import the math library.
import math

# Define the paint_calc function.
def paint_calc(height: int, width: int, cover: int) -> None:
  """Calculate the number of cans of paints needed to paint a wall,
     given a wall height and width."""

  # Calculate and round the number of cans.
  num_cans = (height*width) / cover
  num_cans = int(math.ceil(num_cans))

  # Display the number of cans needed to the user.
  print(f"You'll need {num_cans} cans of paint.")
   
# Obtain the height and width of the wall. Define the coverage variable.
test_h = int(input("Input the height of the wall in m: "))
test_w = int(input("Input the width of the wall in m: "))
coverage = 5

# Invoke the paint_calc function.
paint_calc(height=test_h, width=test_w, cover=coverage)
