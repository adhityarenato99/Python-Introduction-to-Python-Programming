# Problem 3.13. 
# ----------------------------------------------------
# Draw a flowchart for the following problem to determine 
# the grade. There are 3 tests for 3 different subjects. On the basis of grades in 
# the three subjects, M1, M2, and M3, a grade is awarded to each student as 
# per the following rules: 
# a. If the score in each subject is more than 80, and the total is more than 
# 250, the grade is A +
# b. If the score in each subject is more than 60, and the total is more than 
# 200, the grade is A
# c. If the score in any one or more subjects is less than 50, the grade is F
# d. In all other cases, the grade is B. 


# Give the user some context.
print("\nWelcome to grade student calculation")

grade = ''
total = 0

def determineGrade(m1, m2, m3):

    if (m1 < 50 and m2 < 50 and m3 < 50):
        grade = 'F'
        total = m1 + m2 + m3
    elif (m1 > 80 and m2 > 80 and m3 > 80):
        total = m1 + m2 + m3
        if (total > 250):
            grade = 'A+'
        elif (total > 200):
            grade = 'A'
        elif (total < 200):
            grade = 'B'
    elif (m1 > 60 and m2 > 60 and m3 > 60):
        total = m1 + m2 + m3
        if (total > 200):
            grade = 'A'
        elif (total < 200):
            grade = 'B'

    print(total)
    print(grade)


n = ''

while n != 0:

    n = (int(input("Please input student number: ")))

    if n != 0:
        m1 = int(input("\nInput M1: "))
        m2 = int(input("\nInput M2: "))
        m3 = int(input("\nInput M3: "))

        determineGrade(m1, m2, m3)

    elif n == 0:
        print("Thanks again, bye now.")
        exit()
    print()

    # testing is successfully
    # --------------------------
    # print("value of m1 = ", m1)
    # print("value of m2 = ", m2)
    # print("value of m3 = ", m3)