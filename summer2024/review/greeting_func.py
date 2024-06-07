"""
    Greet the user with a randomly chosen greeting.

    Tyler
    6/6/24
"""


# Import the random module.
import random

# Define the greet() function.
def greet():
    """Randomly choose a greeting and display it to the user."""

    # Annotate and define the local variables.
    greeting_list: list[str] = [
        "Hello", "How do you do?", "Lovely weather we're having!",
        "Sup", "How's it going?", "Good morning!", "Howdy!",
        "Hey", "How's life?", "Long time no see!"
        "Nice to meet you", "It's an honor to meet you",
        "Good to see you", "good afternoon", "good evening"
        
]
    greeting: str

    # Randomly choose a greeting from the list.
    greeting = random.choice(greeting_list)

    # Greet the user.
    print(greeting)


# Call the greet() function.
greet()
