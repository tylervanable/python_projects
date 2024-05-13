"""
    Write a program that adds the digits in a 2-digit number.

    e.g. if the input is 35, the output is 8 (3 + 5)

    Tyler
    5/12/24
"""

# Annotate the variables.
two_digit_number: str = input("Please enter a two-digit number: ")
first_digit: str
second_digit: str
sum: int

# Obtain the first and second digits from the two digit number by indexing.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Sum together the first and second digits.
sum = int(first_digit) + int(second_digit)

# Display the sum.
print(sum)
