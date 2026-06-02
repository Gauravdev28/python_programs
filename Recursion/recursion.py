# Here I practise recursion in Python. 
# A recursive function is a function that calls itself in order to solve a problem.
# Recursion == Loops 


# This program is done by using function + loop.
def show(n):
    for num in range(1 , n+1) :
        print(num)

show(5)
print()


# Here I done this function by using Recursion.
def show(n) :
    if (n==0) :
        return
    print(n)
    show(n-1)

show(5)


# Call Stack - When we call multiple stack in single function.
