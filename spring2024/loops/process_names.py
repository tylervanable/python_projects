"""
    Process a file of names.

    Re factoring is when you copy and paste a file and change names of variables

"""


import io

names_file: io.TextIOWrapper # file reference variable
name: str

# Open the files numbers.txt.
names_file = open("names.txt", "r") # path to file name
# above we open the text file, the variable has access to the text file

# Read the first line of the file.
name = names_file.readline()

# While there's data in the file, process, and read.
while name != "":
    # Process the name.
    name = name.strip()
    print(name)
    # Read the next line of the file
    name = names_file.readline()

# Close the file.
names_file.close()

