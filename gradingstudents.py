# HackerLand University has the following grading policy:

# Every student receives a  in the inclusive range from  to .
# Any  less than  is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# Examples

#  round to  (85 - 84 is less than 3)
#  do not round (result is less than 40)
#  do not round (60 - 57 is 3 or higher)
# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

# Function Description

# Complete the function gradingStudents in the editor below.

# gradingStudents has the following parameter(s):

# int grades[n]: the grades before rounding
# Returns

# int[n]: the grades after rounding as appropriate
# Input Format

# The first line contains a single integer, , the number of students.
# Each line  of the  subsequent lines contains a single integer, .

# Constraints

def gradingStudents(grades):
    #initialize rounded grades
    rounded_grades = []
    # Write your code here
    for grade in grades:
        # initialize rounded grade
        rounded_grade = int(round(grade / 5.0) * 5.0)
        # if rounding up to 5 - grade is less than 3 and grade is not less than 38 (because difference between 38 and 40 is less than 3)
        if rounded_grade > grade and (rounded_grade - grade) < 3 and grade >= 38:
            # then round up to 5
            rounded_grades.append(rounded_grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
