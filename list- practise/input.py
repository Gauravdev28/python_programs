# In this program we input the value from user and store in list 
movie = []
mov1 = input("Enter Your First Movie Name : ")
mov2 = input("Enter Your Second Movie Name : ")
mov3 = input("Enter Your Third Movie Name : ")

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)

print(movie)
print(type(movie))


# Other way to add input and direct add in a list by using append 
movie.append(input("Enter Your Fourst Movie Name : "))
print(movie)


