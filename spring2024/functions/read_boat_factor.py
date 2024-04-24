"""
    Read the team names, boat lengths, and transoms from a file called data.txt.
    Then calculate the appropriately sized outboard motor for the boat by
    multiplying the boat length by the transom.
"""


import io

# Annotate the variables.
boat_file: io.TextIOWrapper
team_name: str
boat_length: float
transom: float
factor: int

# Open the data.txt file.
boat_file = open("data.txt", "r")

# Read the first team name or the EOF marker. 
team_name = boat_file.readline().strip()

# Display a message if data.txt is empty and reads an EOF marker.
if team_name == "":
    print("The file contains no boat data.")

while team_name != "":
    boat_length = float(boat_file.readline().strip())
    transom = float(boat_file.readline().strip())
    factor = round(boat_length*transom)

    # Determine the appropriate horsepower depending on factor.
    if 0 <= factor <= 35:
        print("{}, with a factor of {}, requires a motor horsepower of 3."
              .format(team_name, factor))
    elif 36 <= factor <= 39:
        print("{}, with a factor of {}, requires a motor horsepower of 5."
              .format(team_name, factor))
    elif 40 <= factor <= 42:
        print("{}, with a factor of {}, requires a motor horsepower of 7.5."
              .format(team_name, factor))
    elif 43 <= factor <= 45:
        print("{}, with a factor of {}, requires a motor horsepower of 10."
              .format(team_name, factor))
    elif 46 <= factor <= 52:
        print("{}, with a factor of {}, requires a motor horsepower of 15."
              .format(team_name, factor))
    elif factor > 52:
        print("Further calculations are required.")

    # Read the next boat name or EOF marker.
    team_name = boat_file.readline().strip()

# Close the file.
boat_file.close()
