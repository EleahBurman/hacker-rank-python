#in a classroom of n students, find the student with the second lowest grade
#if there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line
#constraints 2<=n<=5 and there will always be one or more students having the second lowest grade
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41],['Harsh', 39]]

###constraint
n = len(students)
if(n<2 or n>5):
    print("n is out of range")
#first line -  n number of students

#nested lists
student_data=[]
student_scores=[]
for i in range(n):

#student's name
    name = students[i][0]
    score = students[i][1]
    student_data.append([name, score])
    student_scores.append(score)
    student_scores.sort()
print("data", student_data)
#student's grade
print("scores", student_scores)

### second lowest
for student_score in student_scores:
    if(student_score>student_scores[0]):
        second_lowest=student_score
        break

print("second lowest score", second_lowest)

### Extract Names
final_list=[]
for [student,score] in student_data:
    if(second_lowest==score):
        final_list.append(student)
        final_list.sort()
print("final list", final_list)

## print names one on top of eachother
for name in final_list:
    print(name)

