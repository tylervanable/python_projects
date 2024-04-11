"""
    A guessing game that:
        Generates a random number between 1 and 100 (import random)
        Allows the user to guess (input)
        Tells the user if their guess is too high or too low (in_range bool function)
        Counts the number of user guesses (accumulator)
        Continues until the user guesses the number (
        Displays the number of guesses once the user has guessed the number (print accumulator)

    Tyler
    4/10/24
"""


import random

def valid_guess(guess: int) -> bool:
    """Generate a random number between 1 and 100 and allow the user
       to guess the number, validate their guess."""
    return guess >= 1 and guess <= 100

def get_user_guess() -> int:
    """Obtain a guess from the user and return the guess."""

    # Annotate the variable.
    guess: int

    # Obtain the guess from the user.
    guess = int(input("What is your guess? "))
    while not valid_guess(guess):
        print("I don't think that's between 1 and 100...")
        guess = int(input("What is your guess? "))
    return guess

def guess_correct(guess: int, number: int) -> bool:
    "Return True if guess is equal to number and False otherwise."""
    return guess == number

def give_hint(guess: int, number: int) -> None:
    """Tell the user if their guess is too low or too high."""
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")


def main() -> None:
    """Play the guessing game with the user until they win."""

    # Annotate some variables.
    number: int
    guess: int
    guess_counter: int = 0

    # Generate a random number between 1 and 100.
    number = random.randint(1, 100)
    
    # Obtain a guess from the user that's between 1 and 100.
    guess = get_user_guess()

    # Add 1 to the guess counter
    guess_counter += 1
    
    # While the guess isn't correct
    while not guess_correct(guess, number):
        
        # Give the user a hint (too high, too low)
        give_hint(guess, number)
        
        # Give them another chance to guess.
        guess = get_user_guess()
        
        # Add 1 to the guess counter
        guess_counter += 1
        
    # If the guess is correct, tell them how many guesses.
    print("You got it! You made {} guesses.".format(guess_counter))

# Invoke the main function.
main()
