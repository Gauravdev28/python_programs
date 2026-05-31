# Here we factorial the number by using function block 

def fact(num) :
    sum = 1
    for i in range(1,num+1) :
        sum = sum*i
    print(sum)
 
fact(5)
     