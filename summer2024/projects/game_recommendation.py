"""
    A program that gives the user a random video game recommendation.
    Users may add video games that will be stored to a list.
    Users may view all of the video games that are stored on the list.

    Tyler
    5/25/24, rev. 5/27/24
"""

# Import the random and io modules.
import random
import io


# Define the choose_game function.
def choose_game(games_list: list[str]) -> str:
    """Choose a random game from the user's game list and return that
       game to the user."""

    # Annotate the local variables.
    chosen_game: str
    random_int: int

    # Choose a random game using the random index.
    chosen_game = random.choice(games_list)

    # Return the chosen game.
    return chosen_game

# Define the add_game function.
def add_game(new_game: str, games_list: list[str]) -> list[str]:
    """Add a new game from the user into the list."""

    # Append the new game to the list.
    games_list.append(new_game)

    # Display a message to the user.
    print(f"{new_game} has been added!")

    # Potentially invoke view_games() here.
    view_games(games_list)
    
    # Return the added game and revised list.
    return games_list

# Define the remove_game function.
    """SOON TO BE IMPLEMENTED"""

# Define the view_games function.
def view_games(games_list: list[str]) -> None:
    """Display the list of games to the user."""

    # Display the list of games to the user.
    print("Here are the game(s) in your game list:")
    print(games_list)
    print()

    # Return to main.
    return
    
# Define the read_games function.
def read_games(games_list: list[str], text_file: str) -> list[str]:
    """Read all the lines of the user's text file and reassign to the games list"""

    # Annotate the local variables.
    read_games_file: io.TextIOWrapper
    current_game: str = "TBD"

    # Open the file in read mode.
    read_games_file = open(text_file, "r")

    # Read the first line of the file.
    current_game = read_games_file.readline().strip()

    # Read and reassign the read values to the games list.
    while current_game != "":
        games_list.append(current_game)
        current_game = read_games_file.readline().strip()
        
    # Close the file.
    read_games_file.close()

    # Return the games list to main.
    return games_list

# Define the write_game function.
def write_game(text_file: str, new_game: str) -> None:
    """Write game names into a text file."""

    # Annotate the local variable.
    write_games_file: io.TextIOWrapper
    
    # Open the file in write mode.
    write_games_file = open(text_file, "a")

    # Write the game name to the text file.
    write_games_file.writelines([new_game, "\n"])

    # Close the file.
    write_games_file.close()

    # Return to main.
    return
    
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
        print("Invalid response. Choose a number.")

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
    text_file: str

    # Obtain a text file name from the user.
    # (soon: use os.path to validate that path exists, otherwise create a file for the user.)
    text_file = input("Enter the name of the text file you wish to use (with no .txt): ")
    text_file = text_file + ".txt"

    # Read the user's text file for any previous games in the list.
    # Assign to the games_list variable.
    games_list = read_games(games_list, text_file)

    # Utilize a sentinel loop so users can continue to utilize the program until
    # they choose to exit.
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
                write_game(text_file, new_game)
                add_game(new_game, games_list)
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

            # Ask if the user would like to continue the program.
            will_continue = continue_program(will_continue)
            print("\n")
            if will_continue == False:
                print("Great! Ending program now...")

        #4.) Display an error message to the user.
        else:
            print("You entered an invalid input. Choose a number.")

# Invoke the main function to start the program.
main()



