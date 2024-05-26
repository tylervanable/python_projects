"""
    A program that gives the user a random video game recommendation.
    Users may add video games that will be stored to a list.
    Users may view all of the video games that are stored on the list.

    Tyler
    5/25/24
"""

# Import the random module.
import random


# Define the choose_game function.
def choose_game(games_list: list[str]) -> str:
    """Choose a random game from the user's game list and return that
       game to the user."""

    # Annotate the local variables.
    chosen_game: str
    random_int: int

    # Choose a random number for the index position of the list.
    random_int = random.randint(0, (len(games_list) - 1))

    # Choose a random game using the random index.
    chosen_game = games_list[random_int]

    # Return the chosen game.
    return chosen_game

# Define the add_game function.
def add_game(new_game: str, games_list: list[str]) -> list[str]:
    """Add a new game from the user into the list."""

    # Append the new game into the games list.
    games_list.append(new_game)
    print(f"{new_game} has been added!")

    # Display all the games in the list to the user.
    view_games(games_list)
    
    # Return the added game and revised list.
    return games_list
    
# Define the view_games function.
def view_games(games_list: list[str]) -> None:
    """Display the list of games to the user."""

    # Display the list of games to the user.
    print("Here are the game(s) in your game list:")
    print(games_list)
    print()

# Define the remove_game function.
    """SOON TO BE IMPLEMENTED"""

# Define the write_game function.
    """SOON TO BE IMPLEMENTED - WRITING TO TXT FILE."""
    
# Define the read_game function.
    """SOON TO BE IMPLEMENTED - READING TO TXT FILE."""
    
# Define the continue_program function.
def continue_program(will_continue: bool) -> bool:
    """Obtain from the user whether or not they wish to continue the program."""

    # Annotate the local variable.
    continue_response: str = "yes"
    
    # Obtain input from the user.
    print("Would you like to continue the program? ")
    continue_response = input("Type yes or no: ")

    # Determine the user's response and store as a bool.
    if continue_response.lower() == "yes":
        will_continue = True
    elif continue_response.lower() == "no":
        will_continue = False
    else:
        print("Invalid response. Run the program again.")

    # Return the bool variable.
    return will_continue

# Display a message to the user, obtain the user's choice for the program,
# and call the appropriate function as needed.
def main() -> None:
    """Obtain the user's choice for the program, to obtain a random game recommendation,
       add a new game to the list, or view the list of games. Will continue to run until
       the user opts to end the program or game is chose."""

    # Annotate the variables.
    games_list: list[str] = []
    user_choice: str
    new_game: str
    add_again: str = "yes"
    will_continue: bool = True
    random_game: str

    # Utilize a sentinel loop so users can continue to utilize the program.
    while will_continue != False:
        
        # Display a message and obtain the user's choice. 
        print("Type 1 to get a random game recommendation, 2 to add a new game to")
        print("the list, or 3 to view all the games from the list.")
        user_choice = int(input("Type 1, 2, or 3: "))
        print()

        # Utilize the user's choice to either - 
        # 1.) Obtain a random game recommendation.
        if user_choice == 1:
            random_game = choose_game(games_list)

            # Display the random game recommendation.
            print(f"The random game chosen is {random_game}!")

            # Ask if the user would like to continue the program.
            will_continue = continue_program(will_continue)
            print("\n")
            if will_continue == False:
                print("Great! Ending program now...")

        # 2.) Add a game recommendation.
        elif user_choice == 2:
            while add_again.lower() == "yes":
                new_game = input("What game would you like to add to the list? ")
                games_list = add_game(new_game, games_list)
                print("Would you like to add another game?")

                # Ask the user if they want to add another game.
                add_again = input("Type yes or no: ")
            
            # Ask if the user would like to continue the program.
            else:
                add_again = "yes"
                will_continue = continue_program(will_continue)
                print()
                if will_continue == False:
                    print("Great! Ending program now...")

        # 3.) View the games in the games list.
        elif user_choice == 3:
            view_games(games_list)

        #4.) Display an error message to the user.
        else:
            print("You entered an invalid input. Choose an option.")
            print(f"{new_game} has been added!")
# Invoke the main function to start the program.
main()



