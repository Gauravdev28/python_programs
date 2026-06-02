# Print list element one by one by using Recursion 

def index_list(list , idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    index_list(list , idx+1)

name = ["Gaurav" , "Rohan" , "Manya" , "Vikul"]
index_list(name)