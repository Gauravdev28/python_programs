# WAP where the program check user number is divisible by 3 and 5 or not 

user = int(input("Enter the number :"))

if (user/3 ==0 and user/5 == 0) :
    print("Number is divisible")
else :
    print("Not Divisible")