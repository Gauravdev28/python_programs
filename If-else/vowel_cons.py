# WAP where we check user input character is vowel or consonant 

user_input = input("Enter the Word :")
vowel = ["a","e","i","o","u"]
if (user_input in vowel) :
    print("Vowel") 
else :
    print("Consonant")