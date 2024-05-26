"""
    Discuss and demonstrate the basics of loops.

    Tyler
    5/25/24
"""

# Annotate the variables.
fruits: list[str]
fruit: str
counter: int = 0

# Make a list of fruits.
fruits = ["Apple", "Peach", "Pear", "Strawberries", "Raspberries"]

# Discuss the basics of the for loop.
print("Let's learn about the 'for' loop.")
print("The basic syntax for a loop is: 'for <item> in <list_of_items>:'.")
print("The result is something happening to each item...")

# Demonstrate a basic loop pattern.
# Display the name of the fruit and 
for fruit in fruits:
    print(fruit)
    counter += 1
    print(f"The count of fruits is now {counter}.")
    print(fruits)

# Insert a line break.
print()

# Discuss what the loop is doing.
print("For each item in the 'fruits' list, in the loop, we are cycling and")
print("assigning the variable 'fruit' until the end of the list.")
print("We are executing the same code within the loop until the loop finishes.")
