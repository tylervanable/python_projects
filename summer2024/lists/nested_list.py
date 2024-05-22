"""
    Demonstrate and discuss an example of a nested list, using the
    'Dirty Dozen' article provided by Dr. Angela Yu.

    We want a list of the 'dirty dozen' crops that use the most
    pesticides. However within that list, we want to separate
    fruits and vegetables.

    Tyler
    5/21/24
"""


# List fruits and vegetables.
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Nest two lists.
dirty_dozen = [fruits, vegetables]

# Display the nested list.
print(dirty_dozen)

# Insert a line break.
print()

# Discuss the nested list.
print("Notice that within the brackets, there are two sets of lists also")
print("contained within a list.")

# Insert a line break.
print()

# Display the first list's second list item from the nested list.
print("To display the nested list's first list, second list item (Nectarines)...")
print("...we must use two indices.")
print("fe: print(dirty_dozen[0][1])")
print("The first index indicates the first list [0] within the nest,")
print("the second index indicates the second list item [1].")
print(dirty_dozen[0][1])

# Insert a line break.
print()

# Display the second list's third list item from the nested list.
print("Similarly, we must use two indicies to access 'Tomatoes'.")
print("The first index is [1], indicating the second list.")
print("The second index is [2], indicating the third list item.")
print("fe: 'print(dirty_dozen[1][2])'.")
print(dirty_dozen[1][2])
