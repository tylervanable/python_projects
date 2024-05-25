"""
    Remove the Wii U from the list of Nintendo consoles.
    Append the Nintendo Switch console into the list.
    Also re-insert the Wii U console to the list.
    Then sort the Nintendo consoles by alphabetical order.
    Finally make a copy of original list.

    Tyler
    5/24/24
"""


# Annotate the variable.
nintendo_consoles: list[str]

# Create a list of some Nintendo consoles by chronological release date.
nintendo_consoles = ["NES", "SNES", "N64", "GameCube", "Wii", "Wii U"]

# Display the list of Nintendo consoles before removing the Wii U.
print("Here is a chronological list of Nintendo consoles prior to 2017:")
print(nintendo_consoles)

# Insert a line break.
print()

# Make a copy of the original list before revisions.
copy_nintendo_consoles = nintendo_consoles.copy()

# Remove the Wii U from the list of Nintendo consoles.
# Display the list of Nintendo consoles.
print("Here is a list of Nintendo consoles, with the removal of the")
print("least profitable Nintendo console.")
nintendo_consoles.remove("Wii U")
print(nintendo_consoles)

# Insert a line break.
print()

# Append the Nintendo Switch into the list.
# Display the revised list.
print("Appending the Switch into the list...")
nintendo_consoles.append("Switch")
print(nintendo_consoles)

# Insert a line break.
print()

# Insert the Wii U back into the list.
# Display the revised list again.
print("Inserting the Wii U into the list...")
nintendo_consoles.insert(5, "Wii U")
print(nintendo_consoles)

# Insert a line break.
print()

# Sort the Nintendo consoles by alphabetical order.
# Display the alphabetized list.
print("Sorting the list of Nintendo consoles by alphabetical order...")
nintendo_consoles.sort()
print(nintendo_consoles)

# Display the original copy for comparison.
print("Displaying the original copy of Nintendo consoles before revisions...")
print(copy_nintendo_consoles)

# Insert a line break.
print()

# Utilize the pop() method to remove Nintendo's least successful console
# in the alphabetically sorted list.
print("Removing the Wii U console using the pop() method...")
nintendo_consoles.pop(6)
print(nintendo_consoles)



