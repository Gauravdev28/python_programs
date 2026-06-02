# Print Number from 1 to n 

def print_num(x):
    if (x==0):
        return
    
    print_num(x-1)
    print(x)

print_num(5)


# Print number from n to 1 

def reverse_num(n):
    if (n==0) :
        return
    
    print(n)
    reverse_num(n-1)

reverse_num(5)