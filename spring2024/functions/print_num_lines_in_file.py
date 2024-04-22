"""
    Write a function that takes a file name as a parameter,
    opens the file, reads and counts all of the lines, and
    returns the number of lines in the file.  Write a main
    function that invokes this function and prints the number
    of lines in the file.

    Tyler
    4/17/24

"""


"""
    Write a function that takes a file name as a parameter, opens the file,
    and reads and returns the first line. If the file doesn't exist, return None.
    Write a main function to invoke this function with a file name and
    display the first line.

    Tyler
    4/17/24
"""


import io
import os.path

def open_file(file_name: str) -> str:
    """Check if file_name exists, open and return if it does, and otherwise
       return None."""

    # Annotate the variable and set its default to None.
    file: io.TextIOWrapper = None
    current_line: str
    line_counter: int = 0

    # Open the file if it exists and return the file, else return None by default
    # if it does not exist.

    # Check if the file exists.
    if os.path.isfile(file_name):
        
        # If the file does exist, open it, read the first line
        # and store the first line as a variable.
        file = open(file_name)
        current_line = file.readline().strip()

        while current_line != "":
            current_line = file.readline().strip()
            line_counter += 1
        
            
    return line_counter

def main() -> None:
    """Invoke the open_file function on files that
       exist and files that don't exist."""

    # Annotate the variables. 
    current_line: str

    # Open first file, read the first line, print it.
    line_counter = open_file("text_text_text_test.txt")

    # Print the first line.
    print("There are {} line(s) in the file.".format(line_counter))

main()

