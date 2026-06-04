# Here we learn how to store data permanently in System by using file handling 
f = open("/Users/gauravagarwal/Documents/GitHub/python_programs/FILEIO/demo.txt" , "r")
# data = f.read()
print(f.read()) # If we read a file it didn't read file again it print blank line 
#print(f.readline()) # It read only single line of our data file

f.close()


# For Writing file 
h = open("write.txt" , "w+")
h.write("My Name is Gaurav Agarwal")
h.close