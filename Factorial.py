def  Factorial(n):
    if n==1:
        return n
    else:
        return n * Factorial(n - 1)
number = int(input ("enter a number "))
if number < 0:
    print("can't be a negative number ")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ", number, " is", Factorial(number) )