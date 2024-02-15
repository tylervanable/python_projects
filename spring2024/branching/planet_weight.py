"""
    Calculate the user's weight on another planet.
    Tyler
    Happy Valentine's Day, 2024
"""


# Define the constants.
MERCURY_WEIGHT: float = 0.38
VENUS_WEIGHT: float = 0.91
EARTH_WEIGHT: float = 1.00
MARS_WEIGHT: float = 2.34
SATURN_WEIGHT: float = 1.06
URANUS_WEIGHT: float = 0.92
NEPTUNE_WEIGHT: float = 1.19
PLUTO_WEIGHT: float = 0.06


# Annotate the variables.
weight: float
planet_name: str
planet_weight: float
valid_planet: bool = True
 
# Obtain the weight and planet from the user.
weight = float(input("What is the weight you want to convert? "))
planet_name = input("What planet? ")

# Calculate the planet's weight.
if planet_name.upper() == "MERCURY":
    planet_weight = weight*MERCURY_WEIGHT
elif planet_name.upper() == "VENUS":
    planet_weight = weight*VENUS_WEIGHT
elif planet_name.upper() == "EARTH":
    planet_weight = weight*EARTH_WEIGHT
elif planet_name.upper() == "MARS":
    planet_weight = weight*MARS_WEIGHT
elif planet_name.upper() == "JUPITER":
    planet_weight = weight*JUPITER_WEIGHT
elif planet_name.upper() == "SATURN":
    planet_weight = weight*SATURN_WEIGHT
elif planet_name.upper() == "URANUS":
    planet_weight = weight*URANUS_WEIGHT
elif planet_name.upper() == "NEPTUNE":
    planet_weight = weight*NEPTUNE_WEIGHT
elif planet_name.upper() == "PLUTO":
    planet_weight = weight*PLUTO_WEIGHT
else:
    valid_planet = False

# Display the weight on the other planet to the user.
if valid_planet:
    print("The weight on {} is {:.2f}.".format(planet_name,planet_weight))
else:
     print("Never heard of this planet...")





# String method operation we can do to strings.
# .upper() or .lower()
