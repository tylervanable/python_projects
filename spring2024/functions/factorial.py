"""
    Write a function that computes the factorial of a positive integer n (n!)
    that is the (parameter) input to the function. n! is defined as
    n * (n-1) * (n-2) * ... * 1. For example, 5! is 5*4*3*2*1, = 120.

    Tyler
    4/3/24
"""


def compute_factorial(n: int) -> int:
    """Compute the factorial of a given value n."""

    # Annotate the variables.
    factorial_value: int = 1
    
    # Calculate the value of the factorial.
    n: int
    while n > 1:
        factorial_value *= n
        n -= 1
        
    # Return the value of the factorial.
    return factorial_value
    
def main() -> None:
    """Obtain the 'n' value from the user for the factorial."""

    # Annotate the variables.
    n: int
    
    # Obtain the value of 'n'.
    n = int(input("Please enter the value of 'n' you wish to factorialize: "))
    
    # Invoke the compute_factorial function.
    factorial_value = compute_factorial(n)

    # Display the value of the factorial for 'n'.
    print("The value of {}! is {}!!!!".format(n, factorial_value))

main()
