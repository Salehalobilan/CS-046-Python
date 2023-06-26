
#print("Hello World"   #here is a (syntaxError) because there is a missing Parenthesis
print("Hello World")  #this is the correct form

#sum = input("Enter the value of sum: ")
#print(sum/0)      #here the Error is (RunTime Error) if it's a string or a number

sum = input("Enter the value of sum: ")
print(sum/1)      #this is the correct form

#print("5^2 =", + 5*2)      #this is a (Logical Error) because 5 power 2 equal 25 not 10
print("5^2 =", + pow(5,2))       #this is the correct form