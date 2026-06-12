# Here I print n number and sum of these number by using recursion 

def sum(num) :
    if (num==0):
        return 0
    
    return num + sum(num-1)

print(sum(5))