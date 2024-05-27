"""
    Calculate the sum of all the even numbers to some user-inputted target
    value.

    Tyler
    5/26/24
"""


# Annotate the variables and obtain the user's input.
target: int = int(input("Enter a target value: "))
sum: int = 0
even: int


# Calculate the sum of all even numbers between 0 and a user-inputted
# target value.
for even in range(0, (target + 1), 2):
    sum += even

# Display the sum to the user.
print(f"The sum of all even numbers between 0 and {target} is {sum}.")
