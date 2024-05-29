"""
    TO-DO list that (will) writes and reads to-do items.
    (Currently only stores to a list until the end of program.)
    Utilizes the datetime library.

    Tyler
    5/28/24, rev. 5/29/24
"""


# Import the io and datetime libraries.
import io
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
        to_do_num = int(input("Enter the number of list item you want to remove: "))

        # Determine which to-do item to remove and remove it.
        to_do_list.pop(to_do_num - 1)

    # Display a message if the user has no list items.
    else:
        print("Could not remove from list. You have no items in your to-do list.")

    # Return the to-do list.
    return to_do_list

# Define the view_list function: 
def view_list(to_do_list: list[str]) -> None:
    """View the list with an input of 2."""

    # Annotate and define the local variable.
    counter: int = 1
    list_item: str

    # If the user has at least one list item,
    if len(to_do_list) >= 1:
    
        # Loop through the length of the list and display the
        # list item number with the each item in the list.
        for list_item in to_do_list:
            
            # Display the do-to list to the user.
            print(f"{counter}. {list_item}")
            counter += 1

    # Display a message if the user has no list items.
    else:
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
    to_do_list: list[str] = []
    day_of_week: str
    week_days: list[str] = ["Mon.", "Tues.", "Wed.", "Thur.", "Fri.", "Sat.", "Sun."]
    months: list[str] = ["January", "February", "March", "April", "May", "June",
                         "July", "August", "September", "October", "November", "December"]
    datetime_list: list[int]

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
    print("Press -1 to QUIT, 0 to ADD a to-do item...")
    print("...1 to REMOVE a to-do item, or 2 to VIEW the list.")

    # Obtain the user's choice for the program's flow.
    user_choice = int(input("Enter -1, 0, 1, or 2: "))
    valid_input = is_valid(user_choice)

    # If the user's input is not valid, close the program.
    if valid_input == False:
        quit_list()

    # If the user enters -1 and the user's input is valid,
    # quit the program.
    while user_choice != -1 and valid_input == True:

        # If the user enters 0, add the user's to do item to the list.
        if user_choice == 0:

            # Obtain the user's to-do item.
            print()
            to_do_item = input("What would you like to add to the to-do list?\n")

            # Add the user's item to the list.
            to_do_list = add_list(to_do_item, to_do_list)

        # If the user enters 1, remove a user's list item from the to-do list.
        elif user_choice == 1:
            print()
            to_do_list = remove_list(to_do_list)

        # If the user enters 2, display the user's list.
        elif user_choice == 2:
            print()
            view_list(to_do_list)

        # Obtain the user's choice for the program's flow.
        print()
        user_choice = int(input("Enter -1, 0, 1, or 2: "))
        valid_input = is_valid(user_choice)

    # If the user enters any other input, display a message.
    else:
        print()
        print("Not a valid input. Please enter either -1, 0, 1, or 2: ")


# Invoke the main() function.
main()
