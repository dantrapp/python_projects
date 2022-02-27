# Create a function that takes student scores from student_scores dict and adds them to a new, empty dict (grades) with the student name and their score (i.e., "Outstanding") in place of the grade.


student_scores = {
    "James": 85,
    "Shannon": 72,
    "Rhia": 97,
    "Jeff": 82,
    "Willow": 89,
    "Rebecca": 78,
    "Jackson": 71,
    "Sam": 83,
    "Foster": 73

}

grades = {}


def grading():
    for k in student_scores:
        if student_scores[k] >= (91):
            grades[k] = "Outstanding"
        elif student_scores[k] <= (90) and student_scores[k] >= 81:
            grades[k] = "Exceeds Expectations"
        elif student_scores[k] <= (80) and student_scores[k] >= 71:
            grades[k] = "Acceptable"
        elif student_scores[k] <= (70):
            grades[k] = "Fail"


grading()

for i in grades:
    print(f"{i} score is: {grades[i]}")
