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

# Remove the Wii U from the list of Nintendo consoles.
# Display the list of Nintendo consoles.
print("Here is a list of Nintendo consoles, with the removal of the")
print("least profitable Nintendo console.")
nintendo_consoles.remove("Wii U")
print(nintendo_consoles)

# Insert a line break.
print()

# Append the Nintendo Switch into the list.
print("Appending the Switch into the list...")
nintendo_consoles.append("Switch")
print(nintendo_consoles)



