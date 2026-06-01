# Number Guessing Game 

while True :
    userinput=(int(input("Enter the Right Number :")))
    num = 7
    while userinput == num :
        print("Correct")
        break
    else :
        print("Guess Again")