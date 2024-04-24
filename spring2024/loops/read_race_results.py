"""
    Read the names, ages, and times in a text file called results.txt.
    Display the name of the winner in each age division in a message to
    the user
"""

import io

# Annotate the variables.
race_file = io.TextIOWrapper
name: str
winner_name_0_to_25: str = ""
winner_name_26_to_100: str = ""
age: int
time: float
fastest_time_0_to_25: float = 0.0
fastest_time_26_to_100: float = 0.0

# Open the file.
race_file = open("results.txt", "r")

# Read the first name or the EOF marker.
name = race_file.readline().strip()

# Display a message to the user if the file is empty.
if name == "":
    print("Nobody completed the race.")

# Read the rest of the file and determine the winners of age divisions
# 0-25 and 26-100.
while name != "":
    age = int(race_file.readline().strip())
    time = float(race_file.readline().strip())
    
    # Determine the winner for the appropriate age division bracket.
    if 0 <= age <= 25:
        if time >= fastest_time_0_to_25:
            fastest_time_0_to_25 = time
            winner_name_0_to_25 = name
            if winner_name_0_to_25 == "":
                winner_name_0_to_25 = "Nobody"
    elif 26 <= age <= 100:
        if time >= fastest_time_26_to_100:
            fastest_time_26_to_100 = time
            winner_name_26_to_100 = name
            if winner_name_0_to_25 == "":
                winner_name_0_to_25 = "Nobody"
                
    # Read the next name or EOF marker.
    name = race_file.readline().strip()

# Display the winners in the two divisions to the user.
print("{} was in the 0-25 age division.".format(winner_name_0_to_25))
print("{} was in the 26-100 age division.".format(winner_name_26_to_100))

# Close the file.
race_file.close()
