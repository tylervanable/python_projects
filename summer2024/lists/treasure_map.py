"""
  Bury treasure in a 3x3 grid. Create a list of three rows of the map and column letters for indexing.
  Nest the rows into a single list. Then index the column using the column letters list.
  Display the buried treasure with an 'X'.

  Tyler
  5/22/24
"""




# List three rows of the map.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

# Nest the three rows into a single list.
map = [line1, line2, line3]

# Display a welcome message to the user.
print("Hiding your treasure! X marks the spot.")

# Obtain the position from the user.
position = input("Where do you want to put the treasure? ")

# Create a list of column letters for indexing purposes.
letters = ["a", "b", "c"]

# Obtain the column index by converting the column letter into
# the appropriate index using the letters list.
column_index = int(letters.index(position[0].lower()))

# Obtain the row index before subtracting 1.
row_index = int(position[1]) - 1

# Insert an 'X' in the appropriate column letter 
map[row_index][column_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
