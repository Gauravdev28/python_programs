# Input a number and find the sum of its digits.

def sum(n) :

    total = 0

    while n>0 :
        digit = n%10
        total = total+digit 
        n = n//10

    print(total)

sum(23)



# Product of Number 

def product (n):
    total = 1

    while n>0 :
        digit = n%10 
        total = total*digit
        n = n//10

    print(total)

product(25)