"""
    Examples of data type manipulation.

    Tyler
    5/12/24
"""


# Annotate the variables
greeting: str
first_char: str
second_char: str
third_char: str
fourth_char: str
fifth_char: str
sixth_char: str

# Assign the index of individual characters to variables.
greeting = "Hello!"
first_char = greeting[0]
second_char = greeting[1]
third_char = greeting[2]
fourth_char = greeting[3]
fifth_char = greeting[4]
sixth_char = greeting[5]

# Display the character to the user with a message.
print("The first character is: " + first_char)
print("The second character is: " + second_char)
print("The third character is: " + third_char)
print("The fourth character is: " + fourth_char)
print("The fifth character is: " + fifth_char)
print("The sixth character is: " + sixth_char)

# Insert line space here.
print()

# When working with large numbers, we can substitute commas with
# underscores.
large_num = int(2_000_000_000 + 1_000_000_000)
print("If we use underscores as commas to add two billion and one billion...")
print("We get the following large number:")
print(large_num)
