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

# Obtain the value of the variables from the user.
adjective = input("Please input an adjective: ")
first_food = input("Please input a food (plural): ")
verb = input("Please input a verb: ")
saying = input("Please input a saying: ")
noun = input("Please input a noun: ")
second_food = input("Please input another food (plural): ")
color = input("Please input a color: ")
vehicle = input("Please input something you would ride in: ")
animal = input("Please input an animal: ")
person = input("Please input a person: ")

# Display the mad-lib to the user.
print("Today I went to my favorite Taco Stand called the {} {}. Unlike most food stands,".format(adjective,animal))
print("they cook and prepare the food in a {} while you {}. The best thing on the menu is the {} {}.".format(vehicle, verb, color, noun))
print("Instead of ground beef, they fill the taco with {}, cheese, and top it off with a salsa made from".format(second_food))
print("{} If that doesn't make your mouth water, then it's just like {} always says: {}!".format(first_food,person,saying))
