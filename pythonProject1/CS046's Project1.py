#************************************************************ #Saleh ALobaylan 443014070 250
todo= ["go to store","study" ,"work on the project", "study"]     #The List
#************************************************************
todo.append("visit my grandmother")        #1
print(todo, " #1")
#--------------------------------------
print(todo.copy(), " #2")                  #2
#--------------------------------------
print(todo.count("study"), " #3")          #3
#--------------------------------------
todo.insert(3,"work")                      #4
print(todo, " #4")
#--------------------------------------
todo.pop(3)                                #5     #here "work" will disappear
print(todo, " #5")
#--------------------------------------
todo.sort()                                #6
print(todo, " #6")
#--------------------------------------
todo.reverse()                             #7
print(todo, " #7")
#--------------------------------------
todo.remove(todo[0]) #first way            #8     #here you remove by index
todo.remove("study") #second way                  #here you remove by the element
print(todo, " #8")
#--------------------------------------
#todo.clear()                               #9
print(todo, " #9")
print("")
#************************************************************ #Saleh ALobaylan 443014070 250
Res= [15,30,13,30,28,29,20,25]     #The List
#************************************************************
print('min: ',min(Res))
print('max: ',max(Res))
print('sum: ',sum(Res))
#--------------------------------------
print('sorted: ',sorted(Res))
#--------------------------------------
print('len: ',len(Res))
#************************************************************ #Saleh ALobaylan 443014070 250
set_Res= {15,30,13,30,28,29,20,25}     #The set List
#************************************************************
print("setRes:", set_Res)
set_Res.add(9)
print("Add number 9 to the set: ", set_Res)
#--------------------------------------
print("eval", eval("3+3"))
#--------------------------------------
ResD= {"stud1":25,"stud2":30}
#--------------------------------------
'''name= input("Enter a name: ")
print("name: ", name.lower())
print("name: ", name.upper())'''
#--------------------------------------
x= round(764.86395,3)
#--------------------------------------
bestStud = "    Faisal, khalid,    Saleh     "
print(bestStud.strip())
#--------------------------------------
Facts = "IT is the best subject to study, IT has many exciting lessons, IT is difficult"
print(Facts)
RealFacts = Facts.replace("IT", "CS")
print(RealFacts)
#--------------------------------------
BestStud= bestStud.split()
print(BestStud)
#--------------------------------------
hashtodo = "#".join(todo)
print(hashtodo)
#--------------------------------------

