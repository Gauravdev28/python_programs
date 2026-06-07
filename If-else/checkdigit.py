# WAP where it check the number is 3 digit numeber or small or big

num = int(input("Enter the Number :"))
if (num <= 0) :
    print("Negative Number")
elif (num >0 and num<10 ): 
    print("One digit Number")
elif(num>9 and num<100) :
    print("It is two digit Number")
elif (num>99 and num<1000):
    print("It is a three digit number")
elif (num >999) :
    print("Greate then 3 digit number")
else :
    print("Invalid")