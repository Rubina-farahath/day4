Num=int(input("enter a integer:"))
count=0
for i in range(1,Num+1):
    if(i%2!=0):
        count=count+1
print("odd numbers are :",count)