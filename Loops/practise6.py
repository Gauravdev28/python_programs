# We using continue or break statement in while loop 
# continue basically skinp the value after the condition true
i = 0

while i <=5 :
    if (i == 3) :
        i+=1
        continue
    print(i)
    i+=1