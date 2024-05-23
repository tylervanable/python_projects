"""
    Reserve a concert seat for the user. Then display their seat choice to the user.

    Tyler
    5/22/24
"""


# Annotate the variables.
row1: str
row2: str
row3: str
row4: str
row5: str
row6: str
seats: list[list[str]]
position: str
letters: list[str]
column_index: int
row_index: int

# List six rows of concert seats.
row1 = ["⬜️","️⬜️","️⬜️", "⬜️️","⬜️️","⬜️️"]
row2 = ["⬜️","⬜️","️⬜️", "⬜️️","⬜️️","⬜️️"]
row3 = ["⬜️️","⬜️️","⬜️️", "⬜️️","⬜️️","⬜️️"]
row4 = ["⬜️","️⬜️","️⬜️", "⬜️️","⬜️️","⬜️️"]
row5 = ["⬜️","⬜️","️⬜️", "⬜️️","⬜️️","⬜️️"]
row6 = ["⬜️️","⬜️️","⬜️️", "⬜️️","⬜️️","⬜️️"]

# Nest the six rows into a single list.
seats = [row1, row2, row3, row4, row5, row6]

# Display a welcome message to the user.
print("Let's purchase concert tickets! X marks your seat.")

# Obtain the position from the user.
position = input("Where do you want to buy a seat? (letter then number) ")

# Create a lst of column letters from indexing purposes.
letters = ["A", "B", "C", "D", "E", "F"]

# Obtain the column index by converting the column letter into
# the appropriate index using the letters list.
column_index = int(letters.index(position[0].upper()))

# Obtain the row index before subtracting 1.
row_index = int(position[1]) - 1

# Insert an 'X' in the appropriate column letter.
seats[row_index][column_index] = "X "

# Display the user's seat.
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}")
