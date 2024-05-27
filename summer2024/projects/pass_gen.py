"""
    Generate a password for the user. Password is semi-random,
    because the password contains first all letters, then all numbers,
    then all symbols.

    Tyler
    5/26/24
"""

# Import the random library.
import random

# Annotate the variables.
num_letters: int
num_numbers: int
num_symbols: int
random_int: int
num_times: int
password: str

# List possible letters, numbers, and symbols for passwords.
letters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols: list[str] = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*' '(', ')', '+', '_', '-', '+', '=', '{', '[', '}', ']', '|']
selected_chars: list[str] = []

# Display a welcome message to the user.
print("Welcome to the PyPassword Generator!")

# Obtain password character requirements from the user.
num_letters = int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# Generate random integers to select random letters in the list.
# Then store as a list.
for letter in range(num_letters):
    random_int = random.randint(0, len(letters) - 1)
    selected_chars.append(letters[random_int])

# Generate random integers to select random numbers in the list.
# Then store as a list.
for number in range(num_numbers):
    random_int = random.randint(0, len(numbers) - 1)
    selected_chars.append(numbers[random_int])

# Generate random integers to select random numbers in the list.
# Then store as a list.
for symbol in range(num_symbols):
    random_int = random.randint(0, len(symbols) - 1)
    selected_chars.append(symbols[random_int])

# Shuffle the order of the selected characters list.
for num_times in range(0, 11):
    random.shuffle(selected_chars)

# Join and display the password.
password = "".join(selected_chars)
print(f"Your password is: {password}.")
    
