"""
    Obtain the city the user grew up in and the name of one of their pets.
    Then display a band name to the user based off the user inputs.

    Adapted from Dr. Angela Yu's "100 Days of Code: The Complete Python
    Pro Bootcamp".

    Tyler
    5/11/24
"""

# Annotate the variables.
city: str
pet_name: str

# Greet the user.
print("Welcome to the band name generator!")

# Obtain a city from the user.
city = input("Please enter the name of the city you grew up in:\n")

# Obtain a name of a pet from the user.
pet_name = input("Please enter a pet name:\n")

# Concatenate the city and pet names and display the user's band name.
print("Your band name is: " + city + " " + pet_name + ".")
