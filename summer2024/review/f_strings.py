"""
    How to use f-strings

    Tyler
    5/13/24
"""


# Annotate the variables.
score: int = 0
height: float = 4.8
winning: bool = True

# Discuss why we want to use f-strings.
print("If I wanted to print the score (an int) with a message (a string)...")
print("...I would get a TypeError")
print('For example: print("Your score is: " + score)')
print("If we wanted no f-strings, we would cast score as a string.")

# Insert line break here.
print()

# Implementing f-strings.
print("To combine multiple data types, we use f strings: ")
print("We must put an 'f' character is front of the string's quotes:")
print('For example: print(f"Your score is: ")')
print("Then we must use curly braces and type the variable name into them:")
print('Then: print(f"Your score is: {score}."')
print(f"Your score is: {score}.")

# Insert line break here.
print()

# Give another example f string.
print(f"Your score is: {score}. Your height is: {height}. \nIt is {winning} that you are winning.")
