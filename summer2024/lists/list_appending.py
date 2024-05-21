"""
    Append "Puerto Rico" into a list of the order of US states by admission
    date into the Union. Then remove "Puerto Rico" from the list.
    Then finally add three fictitious places into the list of states.

    (Note: Puerto Rico is not a US state, but only a contender. This is merely
    an example of list appending.

    Tyler
    5/20/24
"""
# List of states in order by their admission into the Union.
admission_of_states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut',
'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York',
'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana',
'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan',
'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas',
'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota',
'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona',
'Alaska', 'Hawaii']

# Append Puerto Rico into the list of US state admission.
admission_of_states.append("Puerto Rico")
print(admission_of_states)

# Insert a line break.
print()

# Remove Puerto Rico from the list of US state admission.
admission_of_states.remove("Puerto Rico")
print(admission_of_states)

# Insert a line break.
print()

# Use ".extend" to add three fictitious states to the list of states in the US.
print("Let's invite three D&D places into the United States!")
admission_of_states.extend(["Waterdeep", "Neverwinter", "Dragonlance"])
print(admission_of_states)
print("Note: to extend items into a list, list items must be contained")
print("in square brackets.")
