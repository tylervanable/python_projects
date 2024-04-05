"""
    #42. Write a function that converts pounds to kilograms. 1 pound is equal
    to .453492 kilograms. So, for example, if the input were 20,
    the functon would output 9.07184

    Tyler
    4/3/24
"""


def convert_pounds_kilograms(pounds: float) -> float:
    """Calculate the amount of kilograms in some value of pounds."""

    # Annotate the variables.
    kilograms: float
    KILOGRAM_IN_POUND: float = 0.453592
    
    # Calculate the amount of kilograms in pounds.
    kilograms = float(pounds*KILOGRAM_IN_POUND)
    
    # Return the kilogram variable.
    return kilograms

def main() -> None:
    """Obtain the pounds value as a variable from the user"""
    # Annotate the variables.
    pounds: float
    kilograms: float
    
    # Obtain the amount of pounds as a variable from the user.
    pounds = float(input("Please enter the amount of pounds you wish to convert: "))
    
    # Invoke the convert_pounds_kilograms function to conver kilograms in pounds.
    kilograms = convert_pounds_kilograms(pounds)
    
    # Display the amount of kilograms to the user.
    print("{} pounds converts to {} kilograms.".format(pounds, kilograms))

main()
