# Sets is a collection of unordered item 
# Each element must me unique and immutable
# We can't store a value or element double time 
# In set we can not store list or dictonery bcz these are mutable (chagable)
 
number = { 1 , 2 , 3 , 4 , 5 , 5 , 5} # In set they can't print single value in multiple time 
print(number)
print(type(number))
print(len(number)) # In length it count total item in setn but does not count duplicate value 

# Empty set 
number2 = {} # We can't make this as a empty set bcz this is same as dictonery we use same syntex in dict. 
print(type(number2))

# So we write empty set 
number3 = set()
print(type(number3))


# Method of Sets 

# I. Add - In this method we add value  
number4 = {2 , 3 , 4 ,5}
number4.add(7)  # In set we can't add mutable value like list, dict. 
# number4.add([2,3,4])  # It gives error bcz we store list but we store tuples bcz it is immutable 
print(number4)

# II. Remove - It remove particalar value from set 
number5 = {2 , 3 , 5 , 6}
number5.remove(5)  # If we remove unassign value from the set it gives error 
print(number5) 

# III. Clear - It clear the complete set 
number6 = {2 , 3 , 4 , 5 , 6}
number6.add(7)
number6.add(8)
number6.clear() # It clear the all set value make our set null 
print(number6)
print(len(number6))

# IV. POP - It remove random value from set  
number7 = {7 , 10 , 9 , "Gaurav"}
number7.add("Ram")
number7.pop()
print(number7)

# V. Union Method - In this method it combine two set value and make a new set.
setI = {2 , 3 , 4 , 5 , 6}   # It all does not print same value multiple time. 
setII = {5 , 6 , 7 , 8 }
print(setI.union(setII))

# VI. Intersection Method - In this method it print only comman value in both set 
print(setI.intersection(setII))
