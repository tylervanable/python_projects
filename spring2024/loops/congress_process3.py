"""
    Read and process state data recods from a file.
    Records are of the form:
        State name
        number of congressional representatives
        rounded state population
    We assume that all records are complete with two data points per state
"""

import io

# Annotate the variables.
congress_file: io.TextIOWrapper
name: str
num_reps: int
population: int
state_abbr: str
state_accumulate: int = 1

# Open the file of the data or EOF marker.
congress_file = open("congress.txt", "r")

# Read the first state name or EOF marker.
name = congress_file.readline()

# Read and process state data.
while name != "":
    # Read the rest of the record
    num_reps = int(congress_file.readline())
    population = int(congress_file.readline())
    state_abbr = congress_file.readline()
    # Process the record
    name = name.strip()
    if num_reps >= 3 and state_accumulate <= 5:
        state_accumulate += 1
        print("{} has {} representatives, and a population of {}."
            .format(name, num_reps, population))
        print("{}'s state abbreviation is {}".format(name, state_abbr))
    # Read the next state name or EOF marker.
    name = congress_file.readline()

