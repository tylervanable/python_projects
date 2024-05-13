"""
    Type Error examples.

    Tyler
    5/12/24

"""

# Display statements about when the len function will result in a TypeError.
print("When using the built-in len() function, note how we can only concatenate strings using the print() function.")
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
print("Using the len() function, the number of characters in your name is converted to an integer.")
print("The number of characters as an integer is assigned to the variable 'num_char'.")
print('Using: num_char = len(input("What is your name? "))')
num_char = len(input("What is your name? "))

# Insert a line break here.
print("\n")

# Display another message about when code will result in a TypeError.
print("The below code will result in a TypeError:")
print('print("Your name has " + num_char + " characters.")')

# Insert a line break here.
print()

# Display a message to the user about the type() function.
print("We can check the data type of a value/variable using the built-in type() function.")
print("Note: notice how the len() function results in an int.")

# Insert a line break here.
print()

# Display a message about the type of num_char before casting.
print("This is the data type of 'num_char' before casting:")
print(type(num_char))
print('Using: print(type(num_char))')

# Reassign num_char after casting as a string.
print("If we want the above code to work, we must cast 'num_char' into a string.")
print("Because we did not originally cast num_char as a string, we MUST also reassign the casting into 'num_char'.")
num_char = str(num_char)
print('Using: num_char = str(num_char)')

# Display a message to the user about the type of num_char after casting.
print("This is the data type of 'num_char' after casting:")
print(type(num_char))
print('Using: print(type(num_char))')

# Insert a line break here.
print()

# The following concatenated code works after casting:
print("Our code finally works after casting to a string: ")
print('print("Your name has " + num_char + " characters.")')
print("Your name has " + num_char + " characters.")

# Insert a line break here.
print("\n")

# Summarize data type concatenation.
print("In summary, it is NOT possible to concatenate a string and an integer.")
print("It is also NOT possible to concatenate a string and a float.")
print("It IS possible to concatenate two strings, even if the strings contain numbers.")
print("However, it IS possible to concatenate an integer and a float.")

# Insert a line break here.
print()

# Confirming there will be no TypeError between integers and floats.
print("If we try to add a float and an integer, we do NOT get a TypeError.")
print('For example: print(float(10) + int(10))')
print(float(10) + int(10))
print("Note: the result of adding a float and an integer is a float.")

# Insert a line break here.
print()

# Discuss concatenating boolean data types with strings, floats, and integers.
print("If we try to concatenate a string with a bool, we get a TypeError.")
print("If we try to concatenate an integer with a bool, we do NOT get a TypeError.")
print("If we try to concatenate a float with a bool, we do NOT get a TypeError.")
print("If we try to concatenate a bool with a bool, we do NOT get a TypeError.")
