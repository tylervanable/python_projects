"""
    Function bacon_proximity takes the user's birth month (as an integer)
    and birth day (as an integer), takes the absolute difference from Kevin
    Bacon's birth month (July (month 7)) and birth day (8), adds together the
    result, and returns that value.  For example, if the user was born on 12/2,
    the function would add together |7-12| and |8-2|, returning 11 (5+6).
    Use abs() to get the absolute value of the difference.

    Function main is where execution begins (it is called from the global script).
    It takes no parameters and returns no values.  Function main prompts the user
    for their birth month and birth day as integers, calls bacon_proximity with the
    user-entered values as parameters, and displays the result.
"""


def bacon_proximity(birth_month_num: int, birth_day_num: int) -> int:
    """Calculate and return the bacon proximity value by summing the absolute
       values of Kevin Bacon's birth month number (7) subtracted by the user's
       birth month number and Kevin Bacon's birth day number (8) subtracted by
       the user's birth year number (8)."""

    # Define the constants.
    BACON_BIRTH_MONTH_NUM: int = 7
    BACON_BIRTH_DAY_NUM: int = 8
    
    # Return the user's bacon proximity value.
    return (abs(BACON_BIRTH_MONTH_NUM - birth_month_num) +
            abs(BACON_BIRTH_DAY_NUM - birth_day_num))

def main() -> None:
    """Obtain the user's birth month as a number and birth day as a number.
       Then invoke the bacon_proximity and display the result."""

    # Annotate the variables.
    birth_month_num: int
    birth_day_num: int

    # Obtain the user's birth month and birth day as numbers.
    birth_month_num = int(input("Enter your birth month as a number: "))
    birth_day_num = int(input("Enter your birth day as a number: "))

    # Invoke the bacon_proximity function and assign as a variable.
    bacon_result = bacon_proximity(birth_month_num, birth_day_num)

    # Display the bacon proximity result to the user.
    print("Your bacon proximity is {:d}.".format(bacon_result))

main()
