"""
    Given my quiz 1 grade, calculate the points that will be
    removed from my final average. (Quiz 1 = 30% of final grade)

    Tyler
    2/23/24
"""
# Annotate the variables.
QUIZ_PERCENTAGE: float = 0.3

quiz_grade: float
lost_points: float

# Obtain the user's quiz grade.
quiz_grade = int(input("Please input the quiz 1 grade: "))
# If the user inputs a valid quiz grade, calculate and print
# the amount of 30 points lost on the final grade. 
if quiz_grade >= 0 and quiz_grade <= 100:
    lost_points = float(30 - (QUIZ_PERCENTAGE*quiz_grade))
    print("Out of a total of 30 points to your final average, you lost {:.1f} points"
          .format(lost_points))

else:
    print("It seems you entered an invalid test score input...")
    
