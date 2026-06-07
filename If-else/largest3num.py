# WAP where it user input 3 number and it check which one is big 

a = int(input("Enter the Value of A :"))
b = int(input("Enter the Value of B :"))
c = int(input("Enter the Value of C :"))

if (a>b and a>c):
    print(f"A is Greater = {a}")
elif (b>a and b>c) :
    print(f"B is Greate = {b}")
elif (c>a and c>b) :
    print(f"C is Greate = {c}")
else :
    print("Invalid")
