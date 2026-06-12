# Print Number from 1 to n 

def num_print(n):
    if(n==0) :
        return 
    num_print(n-1)
    print(n)
num_print(5)


# Print number from n to 1 

def reverse_num(n):
    if (n==0) :
        return
    
    print(n)
    reverse_num(n-1)

reverse_num(5)