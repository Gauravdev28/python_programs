# Here we find value by user input in tuple 

tup = (1,4,9,16,25,36,49,64,81,100)
index = 0
find = int(input("Enter the number which you find :"))

while index < len(tup) :
    if(tup[index] == find) :
        print("Found" , find)
    index +=1
else :
    print("Not Found")