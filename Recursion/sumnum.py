# Here I print n number and sum of these number by using recursion 

def sum(n):
    if (n < 10):
        return n
    
    return n%10 + sum(n//10)
num = int(input("Enter a number: "))
print("Sum of digits =", sum(num))