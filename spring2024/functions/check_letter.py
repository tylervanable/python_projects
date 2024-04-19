"""
    Write an input validation function that checks if the
    parameter passed (a string of one character) is a letter
    (either between a and z or between A and Z), and returns
    True if it is a letter, and False otherwise.

    is_letter
    input: char: str, the string to check
    processing: check that char is of length 1, if it is, check that
                it's between a-z or A-Z.
    output: True if char is a-z or A-Z, False otherwise, False if
            char is longer than one character
    
    Tyler
    4/17/24
"""

def is_letter(char: str) -> bool:
    """Return True if char is a string of length 1 representing
       a letter."""

    return (len(char) == 1 and
            char.upper() >= "A" and char.upper() <= "Z")


def main() -> None:
        """Invoke is_letter with various characters."""
        print("These tests should all be True:")
        print(is_letter("A"), is_letter("z"), is_letter("A"),
              is_letter("Z"), is_letter("m"), is_letter("N"))

        print()
        
        print("These tests should all be False:")
        print(is_letter("aa"), is_letter(""), is_letter("("),
              is_letter("1"), is_letter("^"), is_letter("2"))

main()
