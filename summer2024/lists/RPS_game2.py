"""
    A rock, paper, scissors game.
    My second try of RPS, after refering to Dr. Yu's example.

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

    Tyler
    5/22/24
"""


# Import the random library.
import random

# Annotate the variables.
rock: str
paper: str
scissors: str
user_choice: str
user_num: int
comp_num: int
comp_choice: str
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

# Obtain either rock, paper, or scissors from the user.
user_num = int(input("Type 0 for rock, 1 for paper, or 2 for scissors: "))
