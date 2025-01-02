Num=int(input("enter a number:"))
rem=0
rev=0
temp=Num
while(Num!=0):
    rem=Num%10
    rev=rev*10+rem
    Num=Num//10
if(temp==rev):
    print("integer is pallindrome")
else:
    print("integer is not a pallindrome")