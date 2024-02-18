""""
Voting Age
Tyler
2/11/24
"""
# Annotate the variable.
age: int

# Obtain the user's age and store as variable.
age = int(input("Please input your age: "))

# Display whether the user is old enough to vote or not.
if age >= 18:
    print("You are old enough to vote!")
else:
    assert age < 18
    print("You are not old enough to vote!")
