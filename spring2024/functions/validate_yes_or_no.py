"""
    Write a function that validates that the user has entered 'yes' or 'no', ignoring
    case. Write a program that asks the user a 'yes' or 'no question, using an input
    validation loop with the function, don't allow the user to continue until they've
    entered 'yes' or 'no'

    Tyler
    4/17/24
"""


def is_valid(response: str) -> bool:
    """Return True if the user entered 'yes' or 'no', ignoring case."""

    return response.lower() == "yes" or response.lower() == "no"


def main() -> None:
    """Invoke is_valid with various responses as test cases."""

    print("These tests should all be True:")
    print(is_valid("yes"), is_valid("YES"), is_valid("Yes"),
          is_valid("No"), is_valid("nO"), is_valid("NO"))

    print()

    print("These tests should all be False:")
    print(is_valid(""), is_valid("!!"), is_valid("perhaps"),
          is_valid("Not"), is_valid("VALID"), is_valid("!@#$%^&*()"))

main()
