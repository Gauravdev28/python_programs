# Find the largest among three numbers using conditions.

a = int(input("Enter Value of A :"))
b = int(input("Enter Value of B :"))
c = int(input("Enter Value of C :"))

if (a>b and b>c) :
    print(f"{a} is Greater then B and C")
elif (b>c and b>a) :
    print(f"{b} is Greater then A and C")
elif (c>a and c>b) :
    print(f"{c} is Greater then A and B")
else :
    print("Invalid")