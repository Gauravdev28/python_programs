# Here we find particular word 
word = "learning"
with open("practise.txt" , "r") as f :
    data = f.read()
    if (data.find(word) != -1) :
        print("Found")
    else :
        print("Not Found")