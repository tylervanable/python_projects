"""
    Check if the user is tall enough to ride a rollercoaster.
    Ask the user if they would like to add a photo for $2.
    If the user is having a mid-life crisis (aged 45-55), they
    the cost of the ticket is free.
    Display the total cost of a ticket.

    Tyler
    5/14/24
"""


# Annotate the variables.
height: int
age: int
bill: int = 0
wants_ticket: str

# Display a message and obtain the height from the user.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Determine if the user can ride the rollercoaster and display the cost
# of the ticket.
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
# Ask the user if they want a picture taken and if they do
# total the total cost of the ticket and photo. 
    wants_ticket = input("Do you want a photo taken? Yes or no: ")
    if wants_ticket.lower() == "yes":
        bill += 3

    # Display the total cost.
    print(f"Please pay: ${bill}.")

# Display a message to the user if they cannot ride the rollercoaster.
else:
    print("Sorry, you have to grow taller before you can ride.")

# Insert a line break.
print("\n")

# Discuss logical operators.
print("Logical operators include: 'and', 'or', and 'not'.")
print("The 'and' operator checks that both two conditions are True.")
print("The 'or' operator checks that at least one of the conditions is True.")
print("While the 'not' operator reverses a condition: True to False; False to True.")

# Insert a line break.
print()

# Exemplify the use of a logical operator.
print("Instead of writing 'elif 45 <= age <= 55:'...")
print("we could have used 'elif age >= 45 and age <= 55:'")

