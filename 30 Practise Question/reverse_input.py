# WAP which reverse the number of user input 


def reverse_num(n) :

    reverse = 0

    while n>0 :
        digit = n%10
        reverse= reverse*10+digit
        n = n//10

    return reverse

print(reverse_num(345))
