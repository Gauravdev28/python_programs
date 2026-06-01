# By using if else conditioin statment we make a calculator

num1 = float(input("Enter the value of A:"))
num2 = float(input("Enter the value of B:"))

operator = input("Enter the Operator:")

if (operator == "+") :
    print("Result :" ,num1+num2 )
elif (operator == "-") :
    print("Result :" , num1-num2)
elif (operator == "*") :
    print ("Result :" , num1*num2)
elif (operator == "/") :
    print ("Result :" , num1/num2)
else :
    print("Invalid Operator")
    