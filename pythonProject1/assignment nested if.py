num = int(input("Enter your final degree: "))
if num >= 90 and num <=100:
    print("your grade is A")
else:
    if num >= 80 and num <=100:
        print("your grade is B")
    else:
        if num >= 70 and num <=100:
            print("your grade is C")
        else:
            if num >= 60 and num <=100:
                print("your grade is D")
            else:
                if num < 60:
                    print("your grade is F")

                else: print("Wrong degree!")


    #This is not a professional way to solve the problem it's more complicated