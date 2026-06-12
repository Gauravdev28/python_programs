# WAP where we print num from user input to 0 

def rever_num(n) :
    if (n==0) :
        return 
    print(n)
    rever_num(n-1)

rever_num(10)