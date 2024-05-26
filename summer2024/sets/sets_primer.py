"""
    Discuss and give examples of sets.

    Tyler
    5/25/24
"""


# Discuss sets.
print("Sets are unordered collections of unique elements.")
print("This means there can only be one representative of the same object.")
print("Sets are unordered, unchangeable, do not allow duplicates.")
print("This means we could not have multiple instances, like '{2, 2, 2, 4, 5}'.")
print("e.g. coords = (item1, item2)")

# Create a set of user ids for some social media website.
user_ids = {1001, 1002, 1003, 1004, 1006}

# Insert a line break.
print()

# Add another user id to the set using the .add() method.
print("Displaying the example set before adding a new value...")
print(user_ids)
user_ids.add(1000)
print("Displaying the example set after adding a new value...")
print(user_ids)
print("Adding a user id of the same value, to demonstrate the no duplicates rule...")
user_ids.add(1000)
print(user_ids)

# Insert a line break.
print()

# Clear the set of user ids.
print("Clearing the set of user ids...")
user_ids.clear()

# Demonstrate the use of lists with sets.
print("Creating a list of user_ids...")
user_id_logins = [1000, 1000, 1000, 1000, 1001, 1001, 1002, 1002, 1003, 1004]
print("Casting the list as a set using set()...")
user_ids = set(user_id_logins)
print(user_ids)
