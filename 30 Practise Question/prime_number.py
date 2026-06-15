# Create a function that checks whether a number is prime.

def prime(n) :

    if n<2 :
        print("Not a Prime Number")
        return

    for i in range (2,n) :
        if (n%i == 0):
            print(f"{n} is not Prime Number")
            break
    else :
        print("It is a Prime Number")

prime(1)