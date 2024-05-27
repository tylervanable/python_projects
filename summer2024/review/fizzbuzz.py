"""
    Print the solution to the FizzBuzz game up to 100.

    Rules:
    - Print each number from 0 to 100 in turn and include 100.
    - When the number is divisible by 3 then print 'Fizz' instead.
    - When the number is divisible by 5 then print 'Buzz' instead.
    - And if the number is divisible by 3 and 5, then print 'Fizz-Buzz' instead.

    Tyler
    5/26/24
"""


# Annotate the variables and define the constant.
TARGET: int = 100
number: int

# Loop through a number including 1 and 100.
for number in range(1, TARGET + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
