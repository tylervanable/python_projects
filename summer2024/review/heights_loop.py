"""
    Calculate and display the total height, number of students, and average height of a list of heights from the user.

    Tyler
    5/25/24
"""

# Annotate the variables.
total_height: int = 0
num_students: int = 0
average_height: float = 0
n: int = 0

# Input a Python list of student heights
student_heights = input("Type a list of heights without commas: ").split()

# Loop through the heights, accumulating the total height, counting the
# number of students, and averaging and displaying the height.
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

for height in student_heights:
    num_students += 1
    total_height += height
    average_height = round(total_height/num_students)
    
# Display the total height, number of students, and average height.
print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {average_height}")

# Display a line break.
print()

# Discuss a note on variable choice.
print("Note: if we want to accumulate the total height from the list...")
print("...remember that the 'height' variable \"holds\" onto each list value...")
print("...before cycling to the next.")

