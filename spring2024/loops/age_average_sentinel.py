"""
    Get ages from the user, display the average age enetered.

    Tyler
    3/25/24
"""



# Annotate the variables.
age_str: str
age: int
total: int = 0
num_ages: int = 0
average: float = 0

# Get the first age from the user or -1. 
age = int(input("Please enter an age or '-1' to quit: "))


# Process ages until the user enters -1. 
while age != -1:
    # Process the age by accumulating it into a total
    # and incrementing the count of ages entered. 
    total += age
    num_ages += 1
    print(age)
    # Get the next age from the user (or -1), EOF. 
    age = int(input("Please enter an age or -1 to quit: "))

# Average the ages entered
if num_ages > 0:
    average = total/num_ages
    print("The average of the ages entered is: {}".format(average))
else:
    print("No ages were entered.")


