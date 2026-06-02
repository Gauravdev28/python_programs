# In tuples it is same as list but it is imutable mean it can't chnage after declaration
# In tuples we write in Bracket in place of Squeare Bracket 
# Note in Tupples we can't print value after assign or in slicing  
tup = (23 , 28 , 20 , 26 , 28 , 20 , 20 )
print(type(tup))
print(tup)

# tup[2] = 5 # This is invalid bcz in tupples we can't change value after declaration 

# I. Index - To find particula value in tupple 
print(tup.index(20))


# II. Count - Count is use to count value how much it used in tupples 

print(tup.count(20))

