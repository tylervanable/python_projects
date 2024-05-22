"""
    Discuss IndexErrors.

    Tyler
    5/21/24
"""


# List the US states in order by their admission into the Union.
admission_of_states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut',
'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York',
'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana',
'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan',
'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas',
'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota',
'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona',
'Alaska', 'Hawaii']

# Using the len() function to determine the number of list items.
num_states = len(admission_of_states)

# Display the number of states in the USA.
print(f"There are {num_states} states in the USA.")

# Insert a line break.
print()

# Discuss a situation in which we would get an IndexError.
print("If we try to use 'num_states' (50) as the index...")
print("...we will get an IndexError.")
print("fe: 'print(admission_of_states[num_states])'.")

# Insert a line break.
print()

# Discuss a remedy to the Index Error, to print the last list item.
print("We can subtract 1 from the 'num_states' index to print the last")
print("list item.")
print("fe: 'print(admission_of_states[num_states - 1])'.")
print(admission_of_states[num_states - 1])

# Insert a line break.
print()

# Discuss indexing.
print("Remember that index start at 0, so we cannot use the number of list items")
print("as the index!")
