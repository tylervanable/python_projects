"""
    Calculate the length of the hypotenuse if a right triangle and
    demonstrate the math library with the distance formula.
    
    Tyler
    ~1/29/24
"""
import math


# Annotate variables
a: float
b: float
distance: float

# Get user input
a = float(input("What is the value of the first side? " ))
b = float(input("What is the value of the second side?" )) 

# Calculate the length of the hypotenuse of the right triangle
# with sides a and b.
distance = math.sqrt(a**2 + b**2)

# Display the hypotenuse length.
print(round(distance, 3))

