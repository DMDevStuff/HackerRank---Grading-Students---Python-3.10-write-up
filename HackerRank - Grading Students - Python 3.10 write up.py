##    https://www.hackerrank.com/challenges/grading/problem
##
##    HackerLand University has the following grading policy:
##
##        Every student receives a grade in the inclusive range from 0 to 100.
##        Any grade less than 40 is a failing grade.
##
##    Sam is a professor at the university and likes to round each student's
##    grade according to these rules:
##
##        If the difference between the grade and the next multiple of 5 is less than 3, 
##        round grade up to the next multiple of 5.
##        If the value of grade is less than 38, no rounding occurs as the result will
##        still be a failing grade.

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the number of grades
#   Algo:
#       iterate and check against the given rules

def gradingStudents(grades):

    rounded_grades = list()

    for grade in grades:

        if grade > 37:

            if grade % 5 > 2:
                rounded_grades.append(grade + (5 - (grade % 5)))

            else:
                rounded_grades.append(grade)

        else:
            rounded_grades.append(grade)

    return rounded_grades
