"""
    Demonstrate use of a for loop without using a list.

    Tyler
    5/26/24
"""


# Discuss for loops independent of lists.
print("When using a for loop independently from a list, we use the")
print("range() function.")

# Insert a line break.
print()

# Discuss the syntax of a for loop using range().
print("for number in range(a, b):")
print("    print(number)")
print("The 'a' is included in the range list.")
print("The 'b' is excluded in the range list.")

# Insert a line break.
print()

# Demonstrate an example of a basic for loop, with a range of 1 through 10.
print("Displaying the numbers 1 through 9 on separate lines using a for loop...")
for number in range(1, 10):
    print(number)
print("Note: if we wanted to display 1 through 10, our range would be")
print("1 through 11.")

# Insert a line break.
print()

# Demonstrate an example of a basic for loop with a stepper.
print("To use a step, our range would look like: 'range(1, 10, 2)'.")
print("The third number in the range, '2' would be our stepper.")
print("Displaying through numbers 1 through 9 on separate lines, stepping every")
print("2 values...")
for number in range(1, 10, 2):
    print(number)

# Display a line break.
print()

# Calculating the total sum of the numbers 1 through 100.
total = 0
total = 0
for number in range(1, 101):
    total += number
print(f"The total is {total}.")
