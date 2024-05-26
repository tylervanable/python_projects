"""
    Calculate the highest score from a list of scores.

    Tyler
    5/26/24
"""


# Annotate the variables.
student_scores: list
n: int = 0
score: int
highest_score: int = 0

# Input a list of student scores, then split the string into a list of strings.
student_scores = input("Type scores without commas, only spaces: ").split()


# Iterate through the list and store the scores as integers.
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Iterate through the list of scores and determine the highest score from the list.
for score in student_scores:
    if score >= highest_score:
        highest_score = score

# Display the highest score.
print(f"The highest score in the class is: {highest_score}")

        
    
    
