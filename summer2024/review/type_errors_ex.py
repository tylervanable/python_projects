"""
    Type Error examples.

    Tyler
    5/12/24

"""

# Display statements about when the len function will result in a TypeError.
print("When using the built-in len() function, note how only strings work.")
print("The following code will result in a TypeError: ")
print('print(len(123))')

# Insert a line break here.
print()

# Display statements about when the len function will NOT result in a TypeError.
print("When printing the number of characters in the string '123', we get:")
print(len("123"))
print('Using: print(len("123"))')
print("Note: there was NOT a TypeError")

# Insert a line break here.
print("\n")

# The following code attempts to obtain a name from the user, convert the
# number of characters into an integer using the len() function, and
# display a message to the user. It will result in a TypeError.
print("Using the len function, the number of characters in your name is converted to an integer.")
print("The number of characters as an integer is assigned to the variable 'num_char'.")
print('Using: num_char = len(input("What is your name? "))')
num_char = len(input("What is your name? "))
print("Note: The number of characters as an integer is assigned to the variable 'num_char'.")

# Insert a line break here.
print()

# Display another message about when code will result in a TypeError.
print("The below code will result in a TypeError:")
print('print("Your name has " + num_char + " characters.")')

# Insert a line break here.
print("\n")

# Display a message to the user about the type() function.
print("We can check the data type of a value/variable using the built-in type() function.")
print("Note: notice how the len() function results in an int.")

# Insert a line break here.
print()

# Display a message about the type of num_char before casting.
print("This is the data type of 'num_char' before casting:")
print(type(num_char))
print('Using: print(type(num_char))')

# Reassigning num_char after casting as a string.
print("If we want the above code to work, we must cast 'num_char' into a string.")
print("We MUST reassign the casting into 'num_char' or assign as a new variable.")
num_char = str(num_char)
print('Using: num_char = str(num_char)')

# Display a message to the user about the type of num_char after casting.
print("This is the data type of 'num_char' after casting:")
print('print(type(num_char))')
print(type(num_char))

# Insert a line break here.
print()

# The following concatenated code works after casting:
print("Our code finally works after casting to a string: ")
print('print("Your name has " + num_char + " characters.")')
print("Your name has " + num_char + " characters.")
