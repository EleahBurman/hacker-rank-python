#store list of students and marks in a dictionary, find the average marks obtained by a student
#name:[marks]
#first line contains integer n - the number of students' records
#the second line contains name and marks obtained by a student each value separated by a space
#final line has query_name - the name a of a student to query
#constrains 2<=n<=10 0<=marks[i]<=100 leng of marks array = 3
#output is print one line the average of marks obtained by the particular student to two decimal places

#sample input
n=3
student_marks = {
    'Krishna': [67, 68, 69],
    'Arjun': [70, 98, 63],
    'Malika': [52, 56, 60]
}
query_name='Malika'

#sample output = 56.00

n=int(input())
student_marks = {}

for student in range(n):
    line = input.split
    name,scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name]=scores
query_name = input()

if query_name in student_marks:
    #average is sum divided by total amount of scores
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(average_score))
else:
    print("Student not found")

print(student_marks)