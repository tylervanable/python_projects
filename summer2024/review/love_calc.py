"""
    Calculate and display the 'love score' of two names that the user inputs.

    To calculate the love score, total the number of times the individual
    characters in both the user-given names occur in the words "TRUE" and
    "LOVE". Combine the first and second number (not add) and that is
    the score.

    Tyler
    5/18/24
"""


# Annotate the variables.
name1: str
name2: str
num_times_true: int = 0
num_times_love: int = 0
love_score: int = 0

# Display a welcome message to the user.
print("Welcome to the Love Calculator!")

# Obtain two names from the user.
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# Display a message to the user before calculations.
print("The Love Calculator is calculating your score...")

# Total the number of times the characters in the word 'true'
# appears in both names.
num_times_true += name1.lower().count("t")
num_times_true += name1.lower().count("r")
num_times_true += name1.lower().count("u")
num_times_true += name1.lower().count("e")
num_times_true += name2.lower().count("t")
num_times_true += name2.lower().count("r")
num_times_true += name2.lower().count("u")
num_times_true += name2.lower().count("e")
first_digit = num_times_true

# Total the number of times the characters in the word 'love'
# appears in both names.
num_times_love += name1.lower().count("l")
num_times_love += name1.lower().count("o")
num_times_love += name1.lower().count("v")
num_times_love += name1.lower().count("e")
num_times_love += name2.lower().count("l")
num_times_love += name2.lower().count("o")
num_times_love += name2.lower().count("v")
num_times_love += name2.lower().count("e")
second_digit = num_times_love

# Concatenate the two digits and cast into an integer.
love_score = int(str(first_digit) + str(second_digit))

# Display a message to the user depending on their love score results.
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
