"""
    User will input string values to create a funny mad-lib story.

    Tyler
    2/7/24
"""

# Define the constants and annotate the variables.
adjective: str
first_food: str
verb: str
saying: str
noun: str
second_food: str
color: str
vehicle: str
animal: str
person: str

# Obtain the words from the user that will be inserted into the mad-lib.
adjective = input("Please input an adjective: ")
animal = input("Please input an animal: ")
vehicle = input("Please input something you would ride in: ")
verb = input("Please input a verb: ")
color = input("Please input a color: ")
noun = input("Please input a noun: ")
second_food = input("Please input another food (plural): ")
first_food = input("Please input a food (plural): ")
person = input("Please input a person: ")
saying = input("Please input a saying: ")

# Display the mad-lib to the user.
print("Today I went to my favorite Taco Stand called the {} {}. Unlike most food stands,".format(adjective,animal))
print("they cook and prepare the food in a {} while you {}. The best thing on the menu is the {} {}.".format(vehicle, verb, color, noun))
print("Instead of ground beef, they fill the taco with {}, cheese, and top it off with a salsa made from {}".format(second_food,first_food))
print("If that doesn't make your mouth water, then it's just like {} always says: {}!".format(person,saying))
