"""
    TO-DO list that writes and reads to-do items.
    Utilizes the datetime library.

    Tyler
    5/28/24, rev. 5/30/24
"""


# Import the io and datetime libraries.
import io
import os
import datetime
from datetime import date

# Define the quit_list function.
def quit_list() -> None:
    """Quit the list with an input of -1."""

    # Display a closing message to the user.
    print()
    print("Be prepared - and come back soon! Closing program...")
    
# Define the add_list function.
def add_list(to_do_item: str, to_do_list: list[str]) -> list[str]:
    """Add to the list with an input or 0."""

    # Append the to-do item into the list.
    to_do_list.append(to_do_item)

    # Return the to-do list.
    return to_do_list

# Define the remove_list function. 
def remove_list(to_do_list: list[str]) -> list[str]:
    """Remove a to-do item from the list."""

    # Annotate the local variable.
    to_do_num: int

    # If the user has at least one list item,
    if len(to_do_list) >= 1:
        
        # Display the list to the user.
        view_list(to_do_list)

        # Obtain the to-do item list number from the user.
        print()
        to_do_num = int(input("Enter the number of list item you want to remove: "))
    
        # Determine which to-do item to remove and remove it.
        to_do_list.pop(to_do_num - 1)

    # Display a message if the user has no list items.
    else:
        print()
        print("Could not remove from list. You have no items in your to-do list.")

    # Return the to-do list.
    return to_do_list

# Define the write_list function.
def write_list(to_do_list: list[str], to_do_item: str, text_file: str) -> None:
    """When the user selects 0 to add a game to the list, write_list will
       write a to-do item into the list."""

    # Annotate the local variable.
    write_to_do_file: io.TextIOWrapper
    next_game: str

    # Open the text file and write in append mode.
    write_to_do_file = open(text_file, "a")

   # Write the game name to the text file.
    for next_game in to_do_list:
        write_to_do_file.write(next_game)
        write_to_do_file.write("\n")
        

   # Close the file.
    write_to_do_file.close()

    # Return to main.
    return

# Define the read_list function.
def read_list(text_file: str) -> list[str]:
    """Read all the games on the text file and save to the to_do_list variable."""

    # Annotate the local variable.
    read_to_do_file: io.TextIOWrapper
    current_line: str
    read_list: list[str] = []

    # Open the file in read mode.
    read_to_do_file = open(text_file, "r")

    # Read the first line of the file.
    current_line = read_to_do_file.readline().strip()

    # Open the text file and read and store the text file.
    while current_line != "":
       read_list.append(current_line)
       current_line = read_to_do_file.readline().strip()

    # Close the file.
    read_to_do_file.close()

    # Return the to-do list.
    return read_list
        

# Define the view_list function: 
def view_list(to_do_list: list[str]) -> None:
    """View the list with an input of 2."""

    # Annotate and define the local variable.
    counter: int = 1
    list_item: str

    # If the user has at least one list item,
    if len(to_do_list) >= 1:

        # Display a message to the user.
        print("Generating your to-do list...")
        # Loop through the length of the list and display the
        # list item number with the each item in the list.
        for list_item in to_do_list:
            
            # Display the do-to list to the user.
            print(f"{counter}. {list_item}")
            counter += 1

    # Display a message if the user has no list items.
    else:
        print()
        print("Could not view the list. You have no items in your to-do list.")
        
    # Return to the program.
    return

# Define the use_datetime() function. 
def use_datetime() -> list[int]:
    """Obtain the date, day, and time and store as variables."""

    # Annotate local variables.
    date: datetime.date
    month: int
    day: int
    year: int

    # Create a date object of today's date.
    today = datetime.date.today()

    # Store the date, month, day, year, and week day index.
    month = today.month
    day = today.day
    year = today.year
    week_day_index = today.weekday()

    # Return the date, month, day, year, and week day index.
    return [month, day, year, week_day_index]

def is_valid(user_choice: int) -> bool:
    """Return True if the user's choice is between -1 and 2 inclusive."""

    # Return True if a choice between -1 and 2 inclusive is entered.
    return -1 <= user_choice <= 2
    
# Obtain the user's choice for how the program will proceed.
def main() -> None:
    """Obtain the user's choice [-1, 0, 1, 2] from the user."""

    # Annotate and define the variables.
    user_choice: int
    valid_input: bool
    to_do_item: str
    to_do_list: list[str] = [""]
    day_of_week: str
    week_days: list[str] = ["Mon.", "Tues.", "Wed.", "Thur.", "Fri.", "Sat.", "Sun."]
    months: list[str] = ["January", "February", "March", "April", "May", "June",
                         "July", "August", "September", "October", "November", "December"]
    datetime_list: list[int]
    text_file: str

    # Determine the month, day, year, and the day of the week.
    # Utilize the datetime library and store values to a list for access.
    datetime_list = use_datetime()
    month = datetime_list[0]
    current_month = months[month - 1]
    day = datetime_list[1]
    year = datetime_list[2]
    week_day_index = datetime_list[3]
    day_of_week = week_days[week_day_index]
    
    # Display a welcome message to the user.
    print("Welcome to your personal to-do list.")
    print(f"Today is {day_of_week} {current_month} {day}, {year}.")
    print()

    # Obtain the name of the user's text file.
    text_file = input("Type the name of your text file: (with no .txt) ")
    text_file = text_file + ".txt"

    # If the user does not have a text file, create a text file.
    if not os.path.isfile(text_file):
        new_file = open(text_file, "x")
        print(f"Created a new text file called {text_file}!")
        new_file.close()

    # Invoke the read_file function to assign contents as a variable.
    to_do_list = read_list(text_file)

    # Display a message to the user before obtaining their choice.
    print()
    print("Press -1 to QUIT, 0 to ADD a to-do item...")
    print("...1 to REMOVE a to-do item, or 2 to VIEW the list.")

    # Obtain the user's choice for the program's flow.
    user_choice = int(input("Enter -1, 0, 1, or 2: "))
    valid_input = is_valid(user_choice)

    
    # If the user enters -1 and the user's input is valid,
    # quit the program.
    while user_choice != -1 and valid_input == True:

        # If the user enters 0, add the user's to do item to the list.
        if user_choice == 0:

            # Obtain the user's to-do item.
            to_do_item = input("What would you like to add to the to-do list?\n")

            # Add the user's item to the list and write it to their text file.
            to_do_list = add_list(to_do_item, to_do_list)
            write_list(text_file, to_do_list, to_do_item)

        # If the user enters 1, remove a user's list item from the to-do list.
        elif user_choice == 1:
            to_do_list = remove_list(to_do_list)

        # If the user enters 2, display the user's list.
        elif user_choice == 2:
            view_list(to_do_list)

        # Obtain the user's choice for the program's flow again.
        print()
        user_choice = int(input("Enter -1, 0, 1, or 2: "))
        valid_input = is_valid(user_choice)

    # If the user enters any other input, display a message.
    if valid_input == False:
        print()
        print("Not a valid input. Next time enter either -1, 0, 1, or 2. ")

        # If the user's input is not valid, close the program.
    else:
        quit_list()


# Invoke the main() function.
main()
        
                      
    
