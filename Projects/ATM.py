# We make a ATM machine which work on Terminal 

Balance = 10000 # User Balance 
ATMPIN = 313 # User ATM PIN 
# Here First we Check ATM PIN 
user_inputpin = int(input("Enter Your ATM PIN :")) 
if ATMPIN == user_inputpin :
    print("Welcome")
    print()
    # Here We Open ATM MENU if user give right ATM PIN otherwise these option not show 
    # These are our ATM Menu 
    while True :
        print("--- ATM Option ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Add Amount ")
        print("4. Exit")
        print()
        choice = int(input("Enter Your Choice :")) 
        # User choice Work 

        if choice == 1 :
            print("Your Account Balance : " ,Balance)

        elif choice == 2 : 
            withdrawl_amount = int(input("Enter Your Withdrawl Amount :"))
            if withdrawl_amount <= Balance :
                print("Your Balance :" , Balance - withdrawl_amount )
            else :
                print("Do not Have sufficient Balance")

        elif choice == 3 :
            add_amount = int(input("Enter Amount For Submit Money :"))
            print("Your Total Amount : " , add_amount+Balance)

        elif choice == 4 :
            print("Exit")

else : 
    print(" Re Enter Your ATM PIN")