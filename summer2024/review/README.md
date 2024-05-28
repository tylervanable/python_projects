Scripts in this directory are adapted from Dr. Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp".

The 'custom_module_ex' directory demonstrates how to import custom Python modules into a script. As an example, 'pi_module' with an approximation of pi is imported into a file called 'import_custom' which prints a variable from the custom module.

The following scripts are review for Python syntax, variables, basic data types, IPO programs, branching (conditionals), loops, and functions:
- 'RPS_game': attempt program for the popular game "Rock, Paper, Scissors"; has not been optimized to utilize lists
- 'add_digits_two_digit': program that requests a two digit number from the user and displays the sum of those individual digits; utilizes indexing of a variable of the integer data type.
- 'band_name': program that asks the user for a city and a name of a pet; it then displays a sample band name to the user
- 'bmi_calc': BMI calculator that requests that user's height in meters and weight in kilograms then displays their BMI
- 'bmi_calc2': similar to the prior program, but instead of simply displaying the user's BMI, the program will also display the clinical interpretation of the user's BMI based on the calculation
- 'data_type_ex': program that demonstrates indexing a variable of the string data type; also demonstrates the use of underscores in place of commas for large numbers (eg 1_000_000 is one million)
- 'f_strings': program that demonstrates the use of displaying text with two different variable types using the f-string
- 'fizzbuzz':
- 'for_loop_no_list':
- 'heads_or_tails': program that demonstrates the use of the random library to generate either a 0 or 1; if the whole number generated is 0, "Tails" is displayed to the user, and if 1, "Heads" is displayed
- 'heights_loop': program that loops through a list of user-inputted heights to calculate and display the total sum of the heights, the average of the heights, and the number of students in the list of heights
- 'highest_score':
- 'leap_year': determines if a user-given year is a leap year and displays whether that year is or is not a leap year
- 'loops_primer': discusses how loops function with lists; how each item in the list is assigned to a iterator variable; this program also iterates through a list of fruits and counts and disaplys the total number of fruits
- 'love_calc': a game program that calculates the "love score" between two user-given names; to find the love score, the program totals the number of times the two names contain the characters in the words "true" and "love"; then the program concatenates the two values; utilizes .lower() and .count()
- 'num_manipulation': program that demonstrates how casting can impact data types such as integers, floats, strings, and bools in Python:
    - Floating point division
    - Integer casting division
    - Fooring division (similar in effect to integer casting division)
    - round() function
    - Augmented operators (+=, -=, *=, /=, **=, //=, %/) and their continuous impact on a variable
- 'odd_or_even': calculates the remainder of the user's number when dividing by 2; displays whether the number is odd or even
- 'pizza_cost': calculates the cost of a pizza order depending on the size of the pizza and the toppings on that pizza
- 'random_module': demonstrates how to obtain a random integer value between 0 and 10 inclusive and how to obtain a random floating point number between 0 inclusive and 1 exclusive; demonstrates the logic behind generating a random floating point number between 0 inclusive and 5 exclusive by multiplying the previously randomly generated floating point number by 5
- 'rollercoaster_height': branching program that requests the user's height in centimeters and prints a message depending on if the user is able to ride a rollercoaster; discusses assignment operators
- 'rollercoaster_height_nested': similar program to the one prior, except it utilizes a nested loop with an elif statement to differentiate how much the user should pay to ride the rollercoaster depending on their age; if the user is younger than 12 years old, they should pay $5, if older than 12 but younger than 18, they should pay $7, and if the user is 18 or older, they should pay $12
- 'rollercoaster_height_total': similar program to the one prior, except it asks the user if they would like a picture taken and if yes, three dollars is added to the cost of the bill; discusses the difference between assignment and an equality check ('=' vs. '=='); utilizes an equality check and .lower()
- 'rollercoaster_midlife': similar program to the one prior, except it allows users having a midlife crisis (between the ages of 45 and 55) to have a free ticket; discusses the use of logical operators, such as 'and', 'or', and 'not'
- 'sum_even_target':
- 'tip_calc': program that calculates the cost of a meal for each person; the user inputs the cost of the meal, what percentage tip they want to give, and between how many people the bill will be split (MY program that I wrote without any additional aid)
- 'tip_calc2': same program as the prior the tip calculator, but includes slight adaptatons from Dr. Yu's Udemy program example; adaptations include an additional variable for readability and use of a format specifier and .format() instead of the round() function
- 'type_errors_ex': program that discusses the TypeError and string concatenation:
    - len() function results in an integer
    - print(len(123)) results in a TypeError
    - Trying to print and concatenate strings and an integer results in a TypeError; must cast int as string
    - type() function displays the data type of what is between the parantheses
    - Bools have two "states", 'True' as '1' or 'False' as '0'; we can add bools with ints, floats, and other bools
- 'weeks_left': a program that asks the user for their age, and calculates how many weeks the user has to live given that they live for 90 years.
- 'your_own_adventure': a game program that is a text, choose-your-adventure story; utilizes multiple IPO patterns and equality checks to guide the user through exploring a wizard's island watchtower 
