grade = int(input("wrtie your grade: "))
total= 0
studnum = 0
while grade > 0:
    total += grade
    studnum += 1
    grade = int(input("wrtie your grade: "))
avr = total / studnum
print("the student grades average is: ",avr)