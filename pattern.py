n=int(input("enter the valuse of n:"))
c=0
num=2
while(c<n):
    for i in range(2,int(num** 0.5)+1):
        if(num%i==0):
            break
    else:
            print((str(num)+ '')*n)
            c+=1
    num+=1
        