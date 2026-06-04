# Here we replace some text from another word in practise.txt file 

with open("practise.txt" , "r") as f :
    data = f.read()

new_data = data.replace("java" , "Python")
print(new_data)

with open("practise.txt" , "w") as f :
    f.write(new_data)