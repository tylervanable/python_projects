"""
    Calculate the length of the hypotenuse if a right triangle and
    demonstrate the math library with the distance formula.
    
    Tyler
    ~1/31/24
"""
import math


# Annotate the variables.
a: float
b: float
distance: float

# Obtain the lengths of 'a' and 'b' of a right triangle from the user.  
a = float(input("What is the value of the first side? " ))
b = float(input("What is the value of the second side?" )) 

# Calculate the length of the hypotenuse of the right triangle.
distance = math.sqrt(a**2 + b**2)

# Display the hypotenuse length.
print(round(distance, 3))

