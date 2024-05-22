"""
    Restaurant Roulette: prompt the user for a string of names, split the string into an
    array, and choose a random person that will pay for the meal using the random library.

    Tyler
    5/21/24

"""

# Import the random library.
import random

# Display a welcome message to the user.
print("Welcome to the Restaurant Roulette, where one (un)lucky person will pay for the bill today!")

# Prompt the user for a list of names.
names_string = input("Enter a list of names, separated by commas, no 'and/or': ")

# Convert the user's string input into an array.
names = names_string.split(", ")

# Generate a random integer between 0 and the length of how many
# names are input minus 1 to account for indexing.
random_whole_num = random.randint(0, (len(names) -1))

# Utilize the random integer as the index of the names list and
# assign the random name to a variable.
random_name = names[random_whole_num]

# Display the random name to the user.
print(f"{random_name} is going to buy the meal today!")
