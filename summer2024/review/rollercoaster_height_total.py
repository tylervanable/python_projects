"""
    Check if the user is tall enough to ride a rollercoaster.
    Ask the user if they would like to add a photo for $2.
    Display the total cost of a ticket.

    Tyler
    5/14/24
"""


# Annotate the variables.
height: int
age: int
bill: int
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

