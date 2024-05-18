"""
    Calculate the user's BMI and display a statement with the clinical
    interpretation of their BMI.

    Tyler
    5/17/24
"""


# Annotate the variables and obtain the user's height and weight.
height: float = float(input("Enter your height in meters: "))
weight: int = float(input("Enter your weight in kilograms as a whole number: "))
bmi: float

# Calculate the user's BMI.
bmi = weight/height**2

# Display a message to the user interpreting their BMI.
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.") 
elif 35 <= bmi:
  print(f"Your BMI is {bmi}, you are clinically obese.")
