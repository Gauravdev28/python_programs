# For loop is used for printing sequential printing of list, tuples , string etc

# Here we print list y using for loop it print value by line by line 
number = [1,4,9,16,25,36,49,64,81,100]

for index in number :
    print(index)

# When we print sting by using for loop it print single word line by line 
string = "Gaurav Agarwal" 

for index in string :
    print(index)


# When we print tuples 

tuple = (1,4,9,16,25,36,49,64,81,100)

for index in tuple :
    print(index) 

# In for loop we have an option for else statement print 
table = [1,2,3,4,5,6,7,8,9,10]

for num in table :
    print(num)
else :
    print("End")


# Concept 

# Range - In range we print number in sequence 
num = range(5) # how much value given in range it print that value like 0 to that value remain it self value  
for seq in num :
    print(seq)

# Other method we write this which is :
# for seq in range(10) : # Here we write 5 in range which is our stop condition
    print(seq)


# Range have three condition (Start,stop,step) where start and step in not complasary but stop condition is mendatory to write 
# Strat + Stop Condition
for seq in range(2,11) :  # Here start value is 2 which is include in print but stop which is 11 which is not include in printing 
    print(seq)


# Start + Stop + Step 
# Step mean size to increase value like +1, +2 which increase the value by that number 

for seq in range(2,21,2) :
    print(seq)


# Pass - Pass keywod use for make a empty loop or skip inside the loop but different as conctinue.

for i in range (11) :
   # Here we want to not declare any thing mean we want to make this loop empty so we don't write here it not work 
   # It show error so we write pass to make this loop empty 
   pass

# We can also use pass in if-else condition to make that loop empty 



