# WAP by using Recurssion to print number from 0 to user input 


def print_num(n) :
    if (n==0) :
        return 
    
    print_num(n-1)
    print(n)

print_num(5)