Num=int(input("enter a integer:"))
count=0
for i in range(1,Num+1):
    if(Num%i==0):
        count=count+1
if(count==2):
    print("it is a prime number:")
else:
    print("not a prime number")
print("-----------------------------------------------------------")
for i in range(2,Num):
    if(Num%i==0):
        print("not a prime number:")
        break
else:
        print("prime number:")
    
