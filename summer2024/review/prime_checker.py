"""
    Determine if a user-given number is prime. Display whether or not it is to
    the user.

    Tyler
    6/7/24
"""

# Define the prime_checker function.
def prime_checker(number: int) -> None:
  """Determine if the user's number is prime. Display to the user."""

  # Annotate the local variable.
  is_prime = True

  # Determine if the number is divisible by 1, itself, or its factor.
  # Assign boolean to is_prime.
  for factor in range(2, number):
    if number % factor == 0:
      is_prime = False
      
# Display a message to the user using is_prime.
  if is_prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
# Obtain a number from the user.
n = int(input("What number do you want the prime number of? "))
prime_checker(number=n)
