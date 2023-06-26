'''print("Hello World!")'''
x = dict(name = "john", age = 36, country = "norway")
print(x)

Dict = {1: " GMC", 2: "tesla",3: "Ford"}
print(Dict[3])
print(Dict.get(2))
Dict["chev"]= "comaro"
print(Dict)

set1 = {"one" ,"two" ,"three" ,"four"}
print(set1)
set1_5 = {3,1,4,2}
print(set1_5)
#Set2 = set("one" ,"two" ,"three" ,"four")

Tuple = ("one", "two","twopoint1", "three")
print(Tuple[0])
Tuple0 = "one", "two","twopoint1", "three"
print(Tuple0[2])
print("\n hello world",end = "")
print("hello Saleh")
L = list("one")
print("\n",L)

if 25>=25.000000000000001: print("\nThey make it clooooser")
print("goodnight\n")

#num = int(input("put an intger: "))
num = 30
if num % 5 == 0:
    print("HI five")
if num % 2 == 0:
    print("Hi even")

if num % 2 == 0:
    print("\neven number")
else:
    print("\nodd number")

if num > 0:
    print("\npositive")
    if num % 5 == 0:
        print("Hi Five!")
    else:
        print("it's not :(")
else:
    print("\nnegitive:(")

#weight = float(input("Enter your weight (kg): "))
#height = float(input("Enter your height(m): "))
weight = 70
height = 1.7
BMI = weight / (height*height)
print("your BMI is: ", BMI)
if BMI < 18.5:
    print("you're Under weight")
elif BMI < 25:
    print("you're normal")
elif BMI < 30:
    print("you're overweight")
else:
    print("obese")

shapes = ["cube","circle", "triangle"]
print("\n")
for L in shapes:
    pass
    print(L,end="-")
    pass
print("\n")
for x in "shapes":
    print(x,end="")
print("\n",L)
print("")
for s in shapes:
    print( s)
    if s =="circle":
        break
print("")
for c in shapes:
    if c == "circle":
        continue
    print(c)


for r in range(13):
    print(r,end="-")
print("")
for r in range(3,25,2):
    print(r, end=">")

print("\n")
for e in range(10):
    print(e)
else:
    print("finishhhhhhhh!")

'''Grade = float(input("Enter the student grade: "))
studnum = 0
total = 0.0
while Grade > -1:
    studnum += 1
    total += Grade
    Grade = float(input("Enter the student grade: "))
avrg= total/studnum
print("\n", "the number of student is: ", studnum,"and thier average grade is: ",avrg)'''
r=1
v=7
for y in range(v):
    for x in range (r):
        print("*",end="")
        v = v-1
    print("")
    r+=1


def plus(x,y):
    return x + y
a = 7
b = 3
plus(a, b)
print(plus(r,weight))

def infinite(*good):
    for e in good:
        e= r*3
        print(e)
infinite(r,shapes,height,num)

print(sorted(set1_5))
#print(sort(set1_5))
print("")
def lamb(fie):
    return lambda user : user  + fie
add_two = lamb(3)
add_five = lamb(5)
char = lamb("Saleh")
print(add_two(200))
print(add_five(50))
print(char("waled"))



#chapter for examples


grades = [90,80,60,45,30]
for g in grades:
    if g >= 60:
        print(g,"Pass!")
    else:
        print(g,"Fail!")

for x in "banana":
    print(x)

for u in shapes:
    print(u)
print("")
for y in shapes:
    print(y)
    if y == "circle":
        break
    print(y)
print("")
for y in shapes:
    if y == "circle":
        break
    print(y)
print("")
for x in shapes:
    if x == "circle":
        continue
    print(x)
print("")
for x in shapes:
    print(x)
    if x == "circle":
        continue
print("")
for x in range(5):
    print(x)
print("")
for x in range(2,6):
    print(x)
print("")
for x in range(2,30,10):
    print(x)
print("")
for x in range(6):
    pass
print("")
for e in range(6):
    print(e)
else:
    print("IDK")
print("")
for e in shapes:
    if e == "circle":
        print(e)
        break
    else: print(e)
else:
    print("Nothing!")

print("")
i=1
while i <= 6:
    print(i)
    i += 1
print("\n",i)
print("")
j = 1
while j < 6:
    print(j)
    if j == 3:
        break
    j += 1
print("")
u= 0
while u <= 6:
    u+= 1
    if u == 3:
        continue
    print(u)
print("")
m= 1
while m< 6:
    print(m)
    m += 1
else:
    print("m is no longer less than 6")
print("\n")
cars = ["tesla","mostange","accent"]
for y in shapes:
    for x in cars:
        print(y,x)
print("")
def greet():
    print("hello")
    return "hello"
greet()
print("")
print(greet())