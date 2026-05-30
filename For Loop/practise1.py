# Here we find x number in our list by using for loop

num = [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number which you find :"))
index = 0 # We print index also 
for find in num :
    if find == x :
        print("Found" ,find , "At Index " ,index)
    index +=1