# Take n as input and find the sum of numbers from 1 to n.

n = int(input("Enter Number :"))
sum = 0
for i in range(1,n+1) :
    sum+=i
    i+=1
    
print(f"Sum of Number {sum} ")