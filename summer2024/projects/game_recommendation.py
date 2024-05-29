"""
    A program that gives the user a random video game recommendation.
    Users may add video games that will be stored to a list.
    Games are written to a text file for use at a later time. 
    Users may view all of the video games that are stored on the list/text file.

    Tyler
    5/25/24, rev. 5/28/24
"""

# Import the random, io, and os.path modules.
import random
import io
import os.path

# Define the read_games function.
def read_games(games_list: list[str], text_file: str) -> list[str]:
    """Read all the lines of the user's text file and reassign to the games list"""

    # Annotate and define the local variables.
    read_games_file: io.TextIOWrapper
    current_game: str = "TBD"

    # Open the file in read mode.
    read_games_file = open(text_file, "r")

    # Read the first line of the file.
    current_game = read_games_file.readline().strip()
    current_game = current_game.title()

    # Read and reassign the read values to the games list.
    while current_game != "":
        games_list.append(current_game)
        current_game = read_games_file.readline().strip()
        current_game = current_game.title()
        
    # Close the file.
    read_games_file.close()

    # Return the games list to main.
    return games_list

# Define the choose_game function.
def choose_game(games_list: list[str]) -> str:
    """Choose a random game from the user's game list and return that
       game to the user."""

    # Annotate the local variable.
    chosen_game: str

    # Choose a random game using the random.choice() method.
    chosen_game = random.choice(games_list)

    # Return the chosen game.
    return chosen_game

# Define the add_game function.
def add_game(new_game: str, games_list: list[str]) -> list[str]:
    """Add a new game from the user into the list."""

    # Append the new game to the list.
    games_list.append(new_game)

    # Display a new game addition message to the user.
    print(f"{new_game} has been added!")

    # Display all the games in the list to the user. 
    view_games(games_list)
    
    # Return the added game and revised list.
    return games_list

# Define the remove_game function.
def remove_game(games_list: list[str], game_to_remove: str, text_file: str) -> list[str]:
    """Remove a game from the user's game list and re-write the text file so to not
       include the removed game."""

    # Define the local variable.
    game: str
    
    # Remove a game from the user's list.
    if game_to_remove in games_list:
        games_list.remove(game_to_remove)

    # Remove the game from the text document by re-writing it.
        with open(text_file, "w") as write_games_file:
            for game in games_list:
                write_games_file.write(game + "\n")

    # Display a message to the user.
        print(f"{game_to_remove} has been removed!")

    else:
        print(f"{game_to_remove} was not found in the list.")
            
    # Return the games list.
    return games_list

# Define the view_games function.
def view_games(games_list: list[str]) -> None:
    """Display the list of games to the user."""

    # Display the list of games to the user.
    print("Here are the game(s) in your game list:")
    print(games_list)
    print()

    # Return to main.
    return

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

    # Annotate and define the local variable.
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
    new_file: str

    # Obtain a text file name from the user.
    text_file = input("Enter the name of the text file you wish to use (with no .txt): ")
    text_file = text_file + ".txt"

    # Check if the text file does not exist or is not in the same directory as the
    # the program. If not, create a file for the user, then close the new file.
    if not os.path.isfile(text_file):
        new_file = open(text_file, "x")
        print(f"Created a new text file called {text_file}!")
        new_file.close()

    # Read the user's text file for any previous games in the list.
    # Assign to the games_list variable.
    games_list = read_games(games_list, text_file)

    # Utilize a sentinel loop so users can continue to utilize the program until
    # they choose to exit.
    while will_continue != False:
        
        # Display a message and obtain the user's choice. 
        print("Type 1 to GET a random game recommendation, 2 to ADD a new game to the list,")
        print("3 to REMOVE a game from the list, 4 to VIEW all the games, or 5 to QUIT.")
        user_choice = int(input("Type 1, 2, 3, 4, or 5: "))
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
                new_game = new_game.title()
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

        # 3.) Remove a game from the games list.
        elif user_choice == 3:

            # Display the user's current game list.
            view_games(games_list)

            game_to_remove = input("What game would you like to remove from the list? ")
            game_to_remove = game_to_remove.title()
            games_list = remove_game(games_list, game_to_remove, text_file)

            # Display the user's current game list.
            view_games(games_list)
            
            # Ask if the user would like to continue the program.
            will_continue = continue_program(will_continue)
            print("\n")
            if will_continue == False:
                print("Great! Ending program now...")
       
        # 4.) View the games in the games list.
        elif user_choice == 4:
            view_games(games_list)

        # 5.) Quit the program.
        elif user_choice == 5:
            will_continue = False
            print("Great! Ending program now...")

        #6.) Display an error message to the user.
        else:
            print("You entered an invalid input. Choose a number.")

# Invoke the main function to start the program.
main()
