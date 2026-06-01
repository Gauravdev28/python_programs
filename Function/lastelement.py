# Here we print last element of list 

list = []
list.append(int(input("Enter the First Value :")))
list.append(int(input("Enter the Second Value :")))
list.append(int(input("Enter the Third Value :")))

def last(list) :
    print(list[-1])

last(list) 