# Here we learn about what is dictonery in Python 
# Dic. are unorder which mean it have no index 
# It is mutable which mean it is changeable 
# We can't create a duplicate keys after declarion one time 
info = {
#    Keys    : Value
    "Name" : "Gaurav Agarwal "  , # We use a comma to seprate or new line 
    "Roll Number" : 99 ,
    "Subject" : ["Python" , "C" , "C++"]

}
info["Name"] = "Ram Agarwal" # Here we change the value outside the dic.
info["Name2"] = "Gaurav Agarwal" # Here we add another info value in dic. 
print(info) # Here we print dictonery single or particular data 

# We can convert dict. into list by using typecasting 

print(type(list(info)))

# Type Of Keys 

# I. Keys - In this word we print all the key without it value 
print(info.keys())
 
# II. Values - In this word we print all the value without its key 
print(info.values())

# III.  Items - This keyword use for print all the dict. data in itmes form. Means particular participation for each element.
print(info.items())

# IV. Get - This keyword use for returning no error if value not exist 
print(info.get("Name3")) # It did not generate error after value is not exist 
print(info["Name2"]) # It show error bcz value not exist 

# V. Update - This keyword use to update our already created dict.
info.update({"City" : "Dholpur" , "Friend" : "Rohan"})
print(info)

# Note - If we create a multiple dict. and if we want to update new dict. into old dict. by using same key name 
info2 = {
    "Name" : "Manya" , 
    "Roll Number" : 139
}

info.update(info2)
print(info)