# Here we make a Mini Calculator which is work in Terminal it do basic function
    # Calcultor Menu 
while True :
    print("-- MINI CALCULATOR --")
    print("1. Addittion")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    print("5. Exit")

    # User Choice 
    choice = int(input("Enter Your Choice :"))

    if choice == 5 :
        print("Exit")
        break 

    # User Input value 
    value1 = int(input("Enter Your Value 1 :"))
    value2 = int(input("Enter Your Value 2 :"))

    # Calculator Working 
    if choice == 1 :
        print("Result : " , value1+value2)
    elif choice == 2 :
        print("Result :" , value1-value2)
    elif choice == 3 :
        print("Result :" , value1*value2)
    elif choice == 4 :
        print("Result :" , value1/value2)
    else : 
        print("Invalid Choice")