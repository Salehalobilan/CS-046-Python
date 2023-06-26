Fac = int(input("Enter a number: "))
def factorial(Fac):
    if Fac == 1:
        return Fac
    else:
        return Fac * factorial(Fac-1)
print("the factorial of",Fac, "is:",factorial(Fac))
