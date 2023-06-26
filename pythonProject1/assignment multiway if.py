num = int(input("Enter your final degree: "))
if num >= 90 and num <= 100:
    print("your grade is A")
elif num >= 80 and num < 90:
    print("your grade is B")
elif num >= 70 and num < 80:
    print("your grade is c")
elif num >= 60 and num < 70:
    print("your grade is D")
elif num > 100:
    print("Wrong degree!")
else:
    print("your grade is F")

    #I like this way of solving the problem more than nested if way
#Saleh Alobaylan