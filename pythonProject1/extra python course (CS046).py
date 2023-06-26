''' Stirngs chapter!! '''
x = 'hello world!'
print(x)
y = "orange"
print(y)
z = '''banana'''
print(z)

s = '''\ni'm 
still 
learning 
python'''
print(s)
inter = "saleh"
'''inter = input("Put your name: ")'''
print("his name is:" , inter)
print("his name is: " + inter.capitalize())

for x in "tesla".capitalize():
    print(x)

text = "python is an important language"
print("importants" in text)

texts = "Python is an important language"
if "python" in texts:
    print("important" in texts)
else:
     print("no",end=" ")

special = " Sa(927319)"
if special.endswith("S"):
    print("good password")
else:
    print("weak\t password")

print(special.index("9"))
print(special.split("927319"),special.split("Sa"),special.split("()"))
print(text.title())
print(text.islower())
GM = special + "hellooooo"
print(GM)
price= 50
Text = "The price is {:.2f} dollars"
print(Text.format(50+200))

atext = "hello world!" [::-2]
print(atext)

def afunction(word):
    return word [::-1]

print(afunction(atext))

list = ["goole", "MS", "oracle" ]
listype = [True , 2, False, "These are diff data type"]
print(listype)
print(len(listype))

#List = list(25,32)
#21نprint(List)

'''thelist = [25, 2, 7,100,10,2,10,7,100]
thelist = list(dict.fromkeys(thelist))
print(thelist)'''


''' Classes and Object chapter!!  '''


class Myclass:
    "the fisrt class ever that i create in python"

print(Myclass.__doc__,"\n")

class do:
    x = 22
    y = 8
    name = "Saleh"

obj = do()
obj2 =do()
print(obj.name, obj.x)
print("his name is",obj.name, "and he is ",obj.x,"years old")
class Myclass:
 def add(slef,x,y):
  return x + y

p1 = Myclass()

print(p1.add(5,6))

##################################################
'''
class Cars:
    def __inf__(self, car_type, car_size):
        self.car_type = car_type
        self.car_size = car_size

    def show(selfs, ob):
        print("car_type: ", ob.car_type)
        print("car_size: ", ob.car_size)

    def add(self car_type, car_size):
        ob = cars(car_type, car_size)
        list.append(ob)
    car_size = "sedan"
    car_type = "small"
    list = []

    obj = cars(car_type, car_size)
    obj.add(car_type,car_size)

    a = input("enter the car type: ")
    b = input("enter the car size: ")
    obj.add(a, b)

    for i in range(list.__len()):
        obj.show(list[i])
   '''

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    def fullname(self):
        return self.first + ' ' + self.last
emp1 = Employee('john','doe',50000)
#emp1+ Employee('jane','doe',60000)

print(emp1.email)
#print(emp.email)

print(emp1.fullname())
