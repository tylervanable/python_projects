"""
    Number manipulation.

    Tyler
    5/13/24
"""


# Discuss floating point division.
print("When we divide two numbers, the result is a float.")
print('For example: print(3/1)')
print("...will result in a float (notice the decimal point).")
print("Result:")
print(3/1)

# Insert space here.
print("\n")

# Discuss integer casting for division.
print("When we divide two numbers and cast the result as an int...")
print('For example: print(int(7/4))')
print("...would normally result as 1.75, if we did not cast as an int.")
print("However, because we casted, any number(s) after the decimal point does not show.")
print("Result:")
print(int(7/4))
print("So instead of a result of 1.75 or 2 (rounded up), we get 1.")
print("Note: we may also cast a decimal number (like 1.75) directly and obtain the same result.")

# Insert space here.
print("\n")

# Discuss flooring division.
print("We have another operator called flooring division.")
print("It calculates how many whole integers there are while dividing two numbers.")
print("For example: print(7//4)")
print("Result:")
print(7//4)
print("You notice similarities between this output and the output when casting an int?")
print("Note: casting division as an int returns the same value as flooring division.")
print("Note: using flooring division, the output is an integer.")

# Insert space here.
print("\n")

# Using the round function.
print("If we want to round 1.75 (7/4) correctly, we use the round() function.")
print('For example: print(int(round(7/4)))')
print("Result:")
print(int(round(7/4)))
print("")
print("Furthermore we can specify to how many decimal places we want to round a float:")
print('For example: print(round(2/3, 2))')
print("...will display 0.67, instead of 0.6 repeating.")
print("Result:")
print(round(2/3, 2))

# Line break here.
print("\n")

# Discuss augmented operators.
print("We can also use augmented operators to change a number/variable by a specific amount.")
print("Try to guess how the 'start' variable is manipulated by these operators:")
print("If: start = 10")
start = 10
print("Example: start += 2")
start += 2
print(start)
print("Example: start -= 2")
start -= 2
print(start)
print("Example: start *= 2")
start *= 2
print(start)
print("Example: start /= 2")
start /= 2
print(start)
print("Example: start **= 2")
start = int(start) # I casted 'start' as an int, because **, //, and % typically result in floats
int(start)
start **= 2
print(start)
print("Example: start //= 2")
start //= 2
print(start)
print("Example: start %= 2")
start %= 2
print(start)
print("Note: the start variable value is changed during each iteration of the augmented operator.")

