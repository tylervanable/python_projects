"""
    Allow the user to enter easy, medium, or hard gamemode.
    Generate a random word and display the number of characters in the word.
    If the user correctly guesses a letter in the word, display the updates.
    If the user does not correctly guess a letter in the word, the user lost a life.
    Iterate until either the word is guessed correctly or the user runs out of lives.

    Currently unfinished, still bug(s)

    Tyler
    6/3/24
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

# Define the find_letters_in_word function.
def find_letters_in_word (random_word: str, user_letter: str, index_positions: list[int]) -> list[int]:
    """Iterate over word to determine the index positions for which the letter appears in the word."""

    # Annotate the local variable.
    char_num: int = 0

    # Iterate over the word and append the index positions of the correct letter to the list.
    for char_num in range(0, len(random_word)):
        if random_word[char_num] == user_letter:
            index_positions.append(char_num)

    # Return the index positions list.
    return index_positions

# Define the update_word function.
def update_word(user_letter: str, index_positions: list[str], dash_list: list[str]) -> str:
    """Update the dashes indicating the number of characters left to the user with the correct letters."""

    # Annotate the local variable.
    index: int

    # Update the dashes.
    for index in range(len(index_positions)):
        dash_list.insert(index, user_letter)
        dash_list.pop(index)

# Annotate and define the variables.
gamemode_choice: int
random_word: str
num_chars: int
dash_display: str
dash_list: list[str] = []
user_letter: str
index_positions: list[int] = []
char_num: int
word_as_list: list[str] = []
life_total: int = 10
already_guessed_letters: list[str] = []

# Import the random and custom wordlist libraries.
import random
from wordlist import easy_words, medium_words, hard_words

# Obtain the gamemode from the user and use the choice to randomly generate a word.
print("Welcome to hangman! Three gamemodes are available: easy, medium, and hard.")
print("Easy is meant for elementary, medium is for middle, and hard is for high school students.")
gamemode_choice = int(input("Type 1 for EASY mode, type 2 for MEDIUM mode, and type 3 for HARD mode: "))
random_word = obtain_random_word(gamemode_choice)

# Obtain and display the length of the random word and the number of dashes to the user.
num_chars = int(len(random_word))
for char_num in range(0, num_chars):
    word_as_list = random_word[char_num]
    dash_list.append("-")
print()
print(f"Your word has {num_chars} letters:")
print(dash_list)

# Obtain a letter from the user and add the characters of the word into a list.
print()
user_letter = input("Type a letter to guess: ").lower()

# Iterate until either the word is completed or the life total is 0.
while life_total != 0 or word_as_list.count("-") == 0:
    
    # If the letter is in the word, update the user's display.
    if random_word.count(user_letter) in word_as_list:
        dash_list = update_word(user_letter, index_positions, dash_list)
        index_positions = find_letters_in_word(random_word, user_letter, index_positions)


    # If the letter is NOT in the word, deduct a point from the user.
    else:
        print(f"'{user_letter.upper()}' is not in your word!")
        life_total -= 1
        print(f"You have {life_total} out of 10 lives left!")

# If the user filled out every letter, conclude the game with a winning message.
if word_as_list.count("-") == 0:
    print("Great work!")

# If the user lost all their points, conclude the game with a losing message.
if life_total == 0:
    print(f"Try again next time! The word was {random_word}")
    



    

    




