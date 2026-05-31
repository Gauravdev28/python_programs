# Here we make a list and count it lenth by using parameters 

cityes =["Dholput" , "Agra", "Gwalior"]
name = ["Gaurav" , "Rohan" , "Vikul"]

def list_name(list):
    print(len(list))

list_name(cityes) 



# No we want to print all city name in single line

def sing_line(list) :
    for single in list :
        print(single , end=" " )

sing_line(cityes)