# In this question we take a user input of subject and make his value as key 

marks = {}
x = int(input("Phy number :" ))
marks.update({"Phy" : x})
y = int(input("Che number :"))
marks.update({"Che" : y})
z = int(input("Math number :"))
marks.update({"Math" : z})

print(marks)