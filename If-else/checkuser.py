# WAP where we check if user id and password is correct or not 

while True :
    id = "admin"
    password = 123

    user_id = input("Enter Your User-Id :")
    user_pass = int(input("Enter Your Password :"))

    if ((user_id and user_pass) == (id and password)) :
        print("Login Successful")
        break
    else :
        print("Invalid User")
