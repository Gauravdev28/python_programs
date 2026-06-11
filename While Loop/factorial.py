# WAP of Factorial of a Number 

factorial = int(input("Enter Number :"))
sum =1
while factorial>0 :
    sum *=factorial
    factorial-=1
print(sum)