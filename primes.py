N=int(input("enter the integer:"))
for i in range(1,N+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)