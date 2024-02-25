"""
Example of a SERIES IF that includes a NESTED IF. ((need to branch after already branching))
    Ask the user whether they'd like a dog, a cat, or other.
    If they choose other, ask them if they'd like a bird or
    a fish or a reptile.
    Print an appropriate message for each choice.
    "A dog is a wonderful companion."

    Tyler
    2/19/24
"""

# Annotate the variables.
pet_choice: str
other_pet_choice: str

# Obtain the user's choice between dog, cat, or other.
pet_choice = input("Pick between a dog, cat, or other: ").lower()

# Print a message if they chose a dog or cat,
# And give them more options if they chose other. 
if pet_choice == "dog":
    print("A dog is a wonderful companion!")
elif pet_choice == "cat":
    print("My cat weighs twenty pounds...!")
elif pet_choice == "other":
    other_pet_choice = input("Pick between a bird, fish, or reptile: ").lower()

    if other_pet_choice == "bird":
        print("Polly want a craacker...?!?")
    elif other_pet_choice == "fish":
        print("Babyy.... shark doo dooooo do do do dooo...")
    elif other_pet_choice == "reptile":
        print("Bet you've seen Jurassic World...")
    else:
        print("I don't know that animal.")    
else:
    print("I don't know that animal")
