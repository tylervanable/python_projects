"""
    Display a table of the user's weight on the planets
    in our solar system.
    Tyler
    Happy Valentine's Day
"""


# Define the constants.
MERCURY_WEIGHT: float = 0.38
VENUS_WEIGHT: float = 0.91
EARTH_WEIGHT: float = 1.00
MARS_WEIGHT: float = 2.34
JUPITER_WEIGHT: float = 2.34
SATURN_WEIGHT: float = 1.06
URANUS_WEIGHT: float = 0.92
NEPTUNE_WEIGHT: float = 1.19
PLUTO_WEIGHT: float = 0.06


# Annotate the variables.
weight: float
planet_weight: float
valid_planet: bool = True
 
# Obtain the weight and planet from the user.
weight = float(input("What is the weight you want to convert? "))

# Display the weight on the other planet to the user.
print("{:15s}{}".format("Planet name", "Weight"))
print("{:15s}{:.2f}".format("Mercury", weight*MERCURY_WEIGHT))
print("{:15s}{:.2f}".format("Venus", weight*VENUS_WEIGHT))
print("{:15s}{:.2f}".format("Earth", weight*EARTH_WEIGHT))
print("{:15s}{:.2f}".format("Mars", weight*MARS_WEIGHT))
print("{:15s}{:.2f}".format("Jupiter", weight*JUPITER_WEIGHT))
print("{:15s}{:.2f}".format("Saturn", weight*JUPITER_WEIGHT))
print("{:15s}{:.2f}".format("Uranus", weight*SATURN_WEIGHT))
print("{:15s}{:.2f}".format("Neptune", weight*NEPTUNE_WEIGHT))
print("{:15s}{:.2f}".format("Pluto", weight*PLUTO_WEIGHT))



