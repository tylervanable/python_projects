"""
    Program that allows users to enter and store the name, address, and
    telephone number of a friend or relative.

    Tyler
    6/13/24
"""


# Define the main() function.
def main() -> None:
    """Obtain a name, address, and telephone number from the user.
       Store them to variables and write to a text document."""

    # Annotate the local variables.
    text_file: str
    name: str = sample_name
    address: str = sample_address
    phone_number: str = sample_number
    book_list: list[dict]
    address_book = {
        "name": name
        "address": address
        "number": phone_number
    }

    # Obtain a text file name from the user.
    text_file = input("Enter a text file name (without .txt): ")

    # Obtain the user's choice for continuing the program.
    print("Type -1 to REMOVE an entry, type 0 to ADD an entry,")
    print("type 1 to EDIT an entry, type 2 to VIEW all entries,")
    print("or type 3 to ERASE all entries.")
    user_choice = input("Enter -1, 0, 1, 2, or 3: ")
    
    # Read the user's past address book.
    ####TODO
    
    # If the user enters -1, cancel the program.
    while user_choice != -1:
        
        # If the user enters 0, obtain a name, address, and phone number
        # from the user. Store to variables, a dictionary, and list.
        # Write the dictionary to a text file.
        if user_choice == 0:
            name.title() = input("Enter the name of a new entry to your address book:\n")
            address = input(f"Enter {name}'s address:\n") 
            phone_number = input(f"Enter {name}'s phone number:\n")
            address_book = add_to_dict()
            book_list.append(address_book)
            write_to_file()

        # If the user enters 1, display the user's current address book.
        # Allow users the opportunity to edit.
        if user_choice == 1:
            a
            
        # If the user enters 2, display the user's current address book.
        if user_choice == 2:
            asd
        # If the user enters 3, delete everything in the text file and the program.
        if user_choice == 3:
            
        # Obtain the user's choice again.
        print("Type -1 to REMOVE, 0 to ADD, 1 to EDIT, 2 to VIEW, or 3 to ERASE.")
        user_choice = input("Enter -1, 0, 1, or 2: ")


    
    
