# WAP where we check user input year is leap year or not 

year = int(input("Enter the Year :"))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")
