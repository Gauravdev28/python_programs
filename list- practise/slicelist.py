# In this program we slice the list and we find particular value in whole list

student_name = ["Gaurav" , "Ram" , "Manya" , "Rohan"] 
print(student_name) # Here we print whole list 
print(student_name[1:3]) #Here we print only selected name  
print(type(student_name))
# In list w have multiple function 
# I. Shorting - if we use sort function it arrange all the data in ascending order 

list = ["Gaurav" , "Ram" , "Orange " , "Apple"] 
print(list.sort())
print(list)

# II. Append - Where we add value in last without taking in list 

print(list.append("Rohan")) #Here it print none and then we print list it pint the list 
print(list)

# III. shorting - In decending order 

list.sort(reverse=True)
print(list)

# IV. Reverse - In this function it reverse all the value 

list.reverse()
print(list)

# V. Insert - In this function we insert the value in particular index

list.insert(3, "Manya")
print(list)

# VI. Remove - In this function we remove the particular given value 

list.remove("Gaurav")
print(list)

# VII. POP - In this function we remove value at particular index

list.pop(2)
print(list)