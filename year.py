Year=int(input("enter a year:"))
if((Year%4==0 and Year%100!=0)or (Year%400==0)):
    print("year is a leap year:")
else:
    print("year is not a leap year:")