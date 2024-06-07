"""
    Greet the user with a randomly chosen greeting. Demonstrates a function
    with an input (with a parameter, the name of the input being passed through
    "name", and an argument, the value of the input being passed through "name".)
    
    Tyler
    6/6/24, rev. 6/7/24
"""


# Import the random module.
import random

# Define the greet() function.
def greet(name: str, location: str):
    """Randomly choose a greeting and display it to the user."""

    # Annotate and define the local variables.
    greeting_list: list[str] = [
        "Hello", "How do you do?", "Lovely weather we're having",
        "Sup", "How's it going", "Good morning", "Howdy",
        "Hey", "How's life", "Long time no see",
        "Nice to meet you", "It's an honor to meet you",
        "Good to see you", "good afternoon", "good evening"
        
]
    greeting: str

    # Randomly choose a greeting from the list.
    greeting = random.choice(greeting_list)

    # Greet the user.
    print(f"{greeting}, {name}")
    print(f"{name}, what is it like in {location}? ")


# Obtain the user's name and location.
name = input("What is your name? ")
location = input("Where are you? ")

# Call the greet() function.
greet(name, location)

# Display a line break.
print()

# Discuss positional arguments.
print("When a function is invoked, it has a positional argument.")
print("This means the order in which the variables are called...")
print("...will impact the order of the variable parameters.")
print("Besides positional arguments, we may also use keyword arguments...")

# Display a line break.
print()

# Demonstrate a function with keyword arguments.
def greet_with(name: str, location: str, weather: str) -> None:
    """Greet the user using keyword arguments."""

    # Display a message to the user.
    print(f"{name}, you are in {location} and the weather looks {weather.lower()}.")


# Annotate the remaining variable.
weather: str

# Obtain user inputs.
name = input("What is your name? ")
location = input("Where are you? ")
weather = input("What's the weather like today? ")
    
# Call the greet_with function using keyword arguments.
greet_with(name=name, location=location, weather=weather)

