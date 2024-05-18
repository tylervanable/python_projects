"""
    Calculate and display the user's BMI.

    Tyler
    5/12/24
"""


# Annotate the inputs and obtain the inputs from the user.
height: float = input("Please enter your height in meters: ")
weight: float = input("Please enter your weight in kilograms: ")

# Annotate the other variable.
BMI: float

# Cast height and weight into a float.
height = float(height)
weight = float(weight)

# Calculate the user's BMI.
BMI = int(weight/height**2)

# Display the user's BMI as an integer.
print(BMI)
