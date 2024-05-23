"""
    A rock, paper, scissors game.

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

# Convert the user's number into a string.
if user_num == 0:
    user_choice = "Rock"
    user_ascii = rock
elif user_num == 1:
    user_choice = "Paper"
    user_ascii = paper    
elif user_num == 2:
    user_choice = "Scissors"
    user_ascii = scissors
else:
    print("Invalid input. Please try again.")
    user_choice = input("Type 0 for rock, 1 for paper, or 2 for scissors: ")

# Generate a random number between 0 and 2.
comp_num = random.randint(0, 2)

# Convert the computer's number into a string.
if comp_num == 0:
    comp_choice = "Rock"
    comp_ascii = rock
elif comp_num == 1:
    comp_choice = "Paper"
    comp_ascii = paper
elif comp_num == 2:
    comp_choice = "Scissors"
    comp_ascii = scissors
    
# Determine the winner of the RPS match.
if user_num == 0 and comp_num == 2:
    is_winner = True
elif user_num == 1 and comp_num == 0:
    is_winner = True
elif user_num == 2 and comp_num == 1:
    is_winner = True
elif user_num == comp_num:
    print("You chose:")
    print(user_ascii)
    print()
    print("Computer chose:")
    print(comp_ascii)
    print()
    print("A draw!")
else:
    print("You chose:")
    print(user_ascii)
    print()
    print("Computer chose:")
    print(comp_ascii)
    print()
    print("You lose!")
if is_winner == True:
    print("You chose:")
    print(user_ascii)
    print()
    print("Computer chose:")
    print(comp_ascii)
    print()
    print("You won!")    

    
