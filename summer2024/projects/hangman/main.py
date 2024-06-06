"""
    Allow the user to enter easy, medium, or hard gamemode.
    Generate a random word and display the number of characters in the word.
    If the user correctly guesses a letter in the word, display the updates.
    If the user does not correctly guess a letter in the word, the user lost a life.
    Iterate until either the word is guessed correctly or the user runs out of lives.

    Tyler
    6/3/24, rev. 6/6/24
"""


# Define the obtain_random_word function.
def obtain_random_word(gamemode_choice: int) -> str:
    """Generate either an easy, medium, or hard-difficulty word and return to the user in main."""

    # If the user selected 1, an easy word is generated.
    if gamemode_choice == 1:
        random_word = random.choice(easy_words)

    # If the user selected 2, a medium-difficulty word is generated.
    elif gamemode_choice == 2:
        random_word = random.choice(medium_words)

    # If the user selected 3, a hard word is generated.
    elif gamemode_choice == 3:
        random_word = random.choice(hard_words)

    # If the user enters an invalid input, display an error message.
    else:
        print("It seems you typed an invalid input. Next time type either 1, 2, or 3.")

    # Return the random word to the user.
    return random_word

# Define the store_word_list function.
def store_word_list (random_word: str) -> list[str]:
    """Store the random word into a list. Return the list."""

    # Annotate the local variable.
    letter: int = 0
    word_as_list: list[str] = []

    # Iterate over the word and append the letters into a list.
    for letter in random_word:
        word_as_list.append(letter.lower())

    # Return the word as a list.
    return word_as_list
        
# Define the update_dash_list function.
def update_dash_list (random_word: str, user_letter: str) -> list[int]:
    """Update dash list order to display to the user."""

    # Annotate the local variable.
    letter_index: int = 0

     # Update the dashes.
    for index, letter in enumerate(random_word):
        if letter == user_letter:
            dash_list[index] = user_letter

    # Return the index positions list.
    return dash_list

# Define the create_dash_list function.
def create_dash_list(random_word: list[str], dash_list: list[str]) -> list[str]:
    """Create the initial dash list of missing characters in the word."""

    # Annotate the local variable.
    dash_list: list[str] = []
    letter_index: int = 0

    # Create the dashes.
    for letter_index in random_word:
        dash_list.append("-")

    # Return the dash list.
    return dash_list

# Annotate and define the variables.
gamemode_choice: int
random_word: str
num_chars: int
dash_list: list[str] = []
user_letter: str
char_num: int
life_total: int = 10
already_guessed_letters: list[str] = []
letter: str
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Import the random and custom wordlist libraries.
import random
from wordlist import easy_words, medium_words, hard_words

# Obtain the gamemode from the user and use the choice to randomly generate a word.
print("Welcome to hangman! Three gamemodes are available: easy, medium, and hard.")
print("Easy is meant for elementary, medium is for middle, and hard is for high school students.")
gamemode_choice = int(input("Type 1 for EASY mode, type 2 for MEDIUM mode, and type 3 for HARD mode: "))
random_word = obtain_random_word(gamemode_choice)

# Save the word as a list of individual characters as strings.
word_as_list = store_word_list(random_word)
print(word_as_list)

# Obtain and display the length of the random word and the number of dashes to the user.
num_chars = int(len(random_word))
dash_list = create_dash_list(random_word, dash_list)
print()
print(f"Your word has {num_chars} letters:")
print(dash_list)

# Obtain a letter from the user and add the characters of the word into a list.
print()

# Until the user runs out of lives or the dash list contains no dashes,
# loop through obtaining a letter and checking it it is in the word.
while life_total != 0:
    user_letter = input("Type a letter to guess: ").lower()
    num_letters = word_as_list.count(user_letter)
    if num_letters == 1:
        print(f"There is a(n) '{user_letter}' in your word.")
        dash_list = update_dash_list(random_word, user_letter)
        print(dash_list)
    elif num_letters > 1:
        print(f"There are {num_letters} '{user_letter}'s in your word.")
        dash_list = update_dash_list(random_word, user_letter)
        print(dash_list)
    else:
        print("There are no '{user_letter}'s in your word.")
        life_total -= 1
        print(f"You have {life_total} lives left!")
    if not "-" in dash_list:
        print("Congratulations! You won! Your word was {random_word}.")
        break
if life_total == 0:
    print(f"Sorry! You lost! Your word was {random_word}.")
