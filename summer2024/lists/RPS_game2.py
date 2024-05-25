"""
    A rock, paper, scissors game.
    My second try of RPS, after refering to Dr. Yu's example.

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

    Tyler
    5/24/24
"""


# Import the random library.
import random

# Annotate the variables.
rock: str
paper: str
scissors: str
user_choice: int
computer_choice: int
is_winner: bool = False
user_ascii: str
comp_ascii: str

# Define ASCII art variables.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Define a list of ASCII art game images.
game_images = [rock, paper, scissors]

# Obtain either rock, paper, or scissors from the user.
user_choice = int(input("Type 0 for rock, 1 for paper, or 2 for scissors: "))

# Determine if the user's number choice is above 2 or below 0 exclusive.
if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:

    # Display a message to the user and an ASCII art game image of the user's choice.
    print("You chose:")
    print(game_images[user_choice])

    # Generate a number between 0 and 2 for the computer's choice.
    # Display a message to the user.
    computer_choice = random.randint(0, 2)
    print(f"The computer chose:")

    # Display an ASCII art game image of the computer's random choice.
    print(game_images[computer_choice])

    # Determine the winner.
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and computer_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif     user_choice == computer_choice:
        print("It's a draw!")


    



