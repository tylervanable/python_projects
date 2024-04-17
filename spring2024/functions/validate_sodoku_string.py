"""
    Write a function that validates that string contains all of the digits
    1 through 9.

    Hint: use len() to ensure the string has 9 characters, and use 'in' to check
    if a value is in the string, e.g. if "1" in string.

    Tyler
    4/17/24
"""


def is_valid(char: str) -> bool:
    """Return True if the char string has a length of 9 characters and contains
       exactly one of each of the following numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9."""
    
    return (len(char) == 9 and
            "1" in char and "2" in char and "3" in char and
            "4" in char and "5" in char and "6" in char and
            "7" in char and "8" in char and "9" in char)

def main() -> None:
    """Invoke is_valid with various strings as test cases."""

    print("These tests should all be True:")
    print(is_valid("123456789"), is_valid("987654321"), is_valid("918273645"),
          is_valid("546372819"), is_valid("456789321"), is_valid("293847561"))

    print()

    print(is_valid(""), is_valid("12345678"), is_valid("1234567890"),
          is_valid("112345678"), is_valid("222222222"), is_valid("191919199"))

main()

          
