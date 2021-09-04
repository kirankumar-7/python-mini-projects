student_scores={
    "Raju":91,
    "Ram":60,
    "Nicolas":82,
    "Kumar":65,
    "Lokesh":78,
    "Hema":70,
}
#creating a empty dictionary
student_grades={}

for student in student_scores:                    #here student is a key 
    score=student_scores[student]
    if score>90:
        student_grades[student]="Outstanding"     #student here is raju his scores is greater than so outstanding
    elif score>80:
        student_grades[student]="Good"
    elif score>70:
        student_grades[student]="Average"
    else:
        student_grades[student]="Fail"
        
print(student_grades)


