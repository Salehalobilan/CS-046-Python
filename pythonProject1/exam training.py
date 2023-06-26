list = ["GMC", "Ford", "Tesla" ]
y = "car"
for x in list:
    print(x, end = " ")
print("\n***********************")
for x in "dainosour":
    print(x, end="")
print("")
print("***********************")
fruits = ["apple","dates", "banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print("***********************")
months = ["jan", "feb", "may", "april"]
for m in months:
    if m == "feb":
        continue
    print(m)
print("***********************")

for metals in range(2,25,2):
    print(metals)
print("***********************")
x= 3
if x>1:
    for metal in range(3):
        print(metal)

    else:
        print("finally finished!")
else:
    print("didn't")
for metal in ["iron", "carbon", "uranuim"]:
    pass
'''print("***********************")
grade= int(input("enter the grade: "))
total = 0
studnum = 0
while grade >= 0:
    total += grade
    studnum = studnum + 1
    grade = int(input("enter the grade: "))
average = total / studnum
print(studnum)'''
print("**********************")
for star in range(3):
    for star in range(8):
        print("^",end="")
    print("")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ")

grade = 105
total = 0
def calc(grade):
    total = 60 + grade
    return total + grade
print(calc(32))
def add(a,b):
    return a + b
j = 5
l = 10
print("Sum of j + l = ", add(j,l))
print("---------------------------")
def infinite(*inf):
    print("the multiply of all this--> ["
          , *inf,"] inputs by 5 is: ")
    for e in inf:
        e= e * 5
        print(e)
infinite(3,2,5,7,8,9,11,12)
print("-----------")
def lamb(n):
    return lambda a: a+n
add2 = lamb(2)
add3 = lamb(3)
char = lamb("A")

print(add2(5))
print(add3(5))
print(char("C"))
