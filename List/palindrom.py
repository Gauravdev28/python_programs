# In this program we solve a palandrom problem 
# (Mean : if we read a table from staring it is same as last we start)

tab = [2 , 3 , 4 , 3 , 2 ]
# table1.reverse()
tab_copy = tab.copy()
tab_copy.reverse()
print(tab)
print(tab_copy)
if(tab == tab_copy) :
    print("Paladrom")
else :
    print("Not a Paladrom")

