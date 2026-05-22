# By using this code we find amount,balance or insufficient balance

balance = 5000
print(balance)
withdrawl= int(input("Enter your Amount of withdraw : "))

if (withdrawl > balance) :
    print("Insufficient balance")
elif (withdrawl < balance) :
    print("Money Deducted : " , balance-withdrawl)
else :
    print("Invalid")