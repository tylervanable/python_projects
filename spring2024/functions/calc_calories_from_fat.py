"""
    A nutritionist who works for a fitness club helps members by evaluating their diets. As
    part of her evaluation, she asks members for the number of fat grams and carbohydrate grams
    that they consumed in a day. Then, she calculates the number of calories that result from
    the fat, using the following formula:
        calories from fat = fat grams * 9
    
    Tyler
    4/15/24
"""


def calc_calories(num_fat_grams: float) -> float:
    """Calculate the value of calories from fat the user consumes in a day and return the amount
       of calories from fat."""

    # Annotate the variable.
    num_calories: float

    # Calculate the number of calories the user gained from fat today.
    num_calories = float(num_fat_grams*9)

    # Return the number of calories the user gained from fat today.
    return num_calories
    
def main() -> float:
    """Obtain the number of fat grams the user consumes in a day and display the amount of
       calories from fat."""

    # Annotate the variable.
    num_fat_grams: float
    num_fat_calories: float

    # Obtain the number of fat grams the user consumed today.
    num_fat_grams = float(input("How many fat grams did you consume today? "))

    # Invoke the calc_calories function to calculate the number of calories.
    num_fat_calories = calc_calories(num_fat_grams)

    # Display the number of calories the user gained today.
    print("The number of calories from fat you consumed today was: {}."
          .format(num_fat_calories))

main()
    
