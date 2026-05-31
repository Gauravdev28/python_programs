# A Function is block of statement that perform specific task again and again to reduce it 
# A Fucnction which have power to reduce code rewrite 
 
# Here we make a block of code which want to use again and again 
# def keyword use to function  
# Function defination 
def cal_sum(a ,b) : # Function paramenters 
    return a+b

    
# Here we call the function code without rewrite only passing value 
cal_sum(4,6) # Function calling 


# Note - if we want to use function multiple time and store the value of multiple function we use return 
# If we use print it give answer but did't store value of a and b its only print one time if we call it again it generate error 


def cal_sum(a ,b) : # Function paramenters 
    #print(a+b) 
    return a+b # It give answer 
    
sumx = cal_sum(8 ,6) # Function calling   # it will done by print function but we want to print it in 2 or more statement we want to use return value 
print(sumx)


sumy = 10+sumx
print(sumy)




# Function Have two type 
# 1. Built in Function (Lenth , )
# 2. User defined Function 


# Default Parameter - It is used for make a function empty mean where we pass argument empty 

def cal_mul (a=1, b=1) :# This is called default parameter here we already give default value 
    print(a*b)
    return a*b

cal_mul() # here we remain the argument empty 