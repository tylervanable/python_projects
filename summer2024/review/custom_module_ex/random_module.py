"""
    Demonstrate the import library.
    Demonstrate how to import a custom module.

    Tyler
    5/19/24
"""

# Import the random library.
import random

# Import a custom library called pi_module.
import pi_module

# Generate a random whole number between 1 and 10 inclusive.
random_integer = random.randint(1, 10)
print("Generating a whole number between 0 and 10 inclusive...")
print(random_integer)

# Generate a random floating point number between 0 inclusive and 1 exclusive.
random_float = random.random()
print("Generating a floating point number between 0 inclusive and 1 exclsuive...")
print(random_float)

# Generate a random floating point number between 0 inclusive and 5 exclusive.
print("We can generate a floating point number between 0 inclusive and 5 exclusive by...")
print("...multiplying our 'random_float' variable by 5.")
random_float *= 5
print(random_float)

# Insert a line space.
print()

# Display a variable called 'pi' from the custom 'pi_module'.
print("The name of the custom module is 'pi_module'.")
print("The name of the custom variable is 'pi'")
print("If we import pi_module, Writing 'pi_module.pi' will print")
print("the variable from our custom module:")
print(pi_module.pi)


