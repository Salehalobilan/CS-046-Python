grade = int(input("type your grade: "))
avrg = 0
studnum = 0
grades = 0
while grade > -1:

    studnum = studnum + 1
    grades += grade
    grade = int(input("type your grade: "))

avrg = grades / studnum
print("the avrage is: ", avrg)
