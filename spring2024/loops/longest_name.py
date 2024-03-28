"""
    Write a loop that gets five names from the user and
    finds the longest name.
    You can find the length of a word using len, e.g.g.
    len("hello") is 5.
"""
import sys

# Annotate and initialize the variables
name: str = ""
longest_name: str = ""
longest_name_num_char: int = -sys.maxsize-1
i: int = 0

# Initialize the loop.
while i < 5:
    # Obtain a name from the user.
    name = input("Please input a name: ")
    # Initialize a nested loop to determine if the length
    # of the name contains the largest number of characters. 
    if len(name) > longest_name_num_char:
        longest_name = name
        longest_name_num_char = len(longest_name)
    i += 1

# Display the longest name to the user.
print("The longest name is {}".format(longest_name))
        
    
