# Find the largest number where we input two number 
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
if (a>b):
    print("A is greater then B :" ,a)
elif (b>a):
    print("B is greater then A :" ,b)
elif (a==b):
    print("A and B both are Equal")
else :
    print("Invalid")