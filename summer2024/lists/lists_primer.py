"""
  Discuss lists, give an example of lists, and demonstrate the basics of using lists.

  Tyler
  rev. 5/25/24
"""


# Discuss lists.
print("A list is a data structure, used to store related, like items together.")
print("Lists have a particular order.")
print("However lists are mutuable, meaning they can be changed.")
print("List items are separated by commas and surrounded by square brackets.")
print("e.g. fruits = [item1, item2]")

# Insert a line break.
print()

# List of states in order by their admission into the Union.
admission_of_states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut',
'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York',
'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana',
'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan',
'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas',
'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota',
'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona',
'Alaska', 'Hawaii']

# Display the first state in the list, Delaware.
print("To display the first state that was admitted...")
print("...we type 'print(admission_of_states[0])'.")
print("Note: we print the variable name of the list, with square brackets around index 0.")
print("Note: we can assign 'admission_of_states[0] to a variable, like 'first_state'.")
print("The first state is index 0, the second state is index 1, third at index 2, etc.")
print("Displaying the first admitted state:")
print(admission_of_states[0])

# Display the second state in the list, Pennsylvania.
print("Displaying the second admitted state:")
print(admission_of_states[1])

# Insert a line break.
print()

# Display the last state in the list, Hawaii.
print("To display the last state that was admitted...")
print("...we type 'print(admission_of_states[-1]'.")
print("Note: using an index of -1 means that last item in the list.")
print("Displaying the last admitted state:")
print(admission_of_states[-1])

# Display the second to last state in the list, Alaska.
print("Displaying the second to last admitted state:")
print(admission_of_states[-2])

# Insert a line break.
print()

# Rename a list item.
print("The full name of 'Pennsylvania' is the 'Commonwealth of Pennsylvania'.")
print("Let's rename list item, index 1, to its full legal name...")
print("...to do so, we assign the new name to the list name at index 1.")
print("It would look like: 'admission_of_states[1] = \"The Commonwealth of Pennsylvania\"'.")
print("Renaming 'Pennsylvania' to its full name and displaying the change:")
admission_of_states[1] = "The Commonwealth of Pennsylvania"
print(admission_of_states[1])



