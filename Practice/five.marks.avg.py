# WAP to take a input of five subject number and find the avg. 

eng = float(input("Enter Your English Marks :"))
bio = float(input("Enter Your Biology Marks :"))
chem = float(input("Enter Your Chemistry Marks :"))
phy = float(input("Enter Your Physics Marks :"))
math = float(input("Enter Your Math Marks :"))


avg = ((eng+bio+chem+phy+math) /3)

print("Average of Five Subject Number is :" , round(avg,2))