""" 
    Obtain the user's name and lucky number and print a message.
    
    Tyler
    1/24/24
"""


# Annotate the variables.
name: str
lucky_number: int

# Obtain the user's name and lucky number.

name = input("Please enter your name: ")
lucky_number = int(input("What's your lucky number? "))

# Print a message. 
print("{}, {} is a very lucky number!".format(name, lucky_number))
