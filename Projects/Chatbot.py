def chatbot() :
    print("AI Chatbot")

while True :
    user = input("You :")

    if user == "Hello" :
        print("Bot : Hi ")
    
    elif user == "How are You" :
        print("Bot : I'm fine, thanks!")
    
    elif user == "bye" :
        print("Goodbye!")
        break 
    else :
        print("Input is Incorrect")

chatbot()