# How many times did the user enter a number before deciding to stop by entering 0?

while True :
    userinput = int(input("Enter the Number :"))

    while userinput == 0 :
        print("Found")
        break 
    else :
        print("Enter Again")