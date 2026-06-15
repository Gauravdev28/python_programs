# Create a function that returns the factorial of a number.

def fact(n) :
    total = 1
    for i in range(1,n+1):
        total *= i
        i+=1
    print(total)

fact(5)