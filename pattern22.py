n=int(input("enter a number:"))
x=1
for i in range(n):
    for j in range(n):
        print(x,end="")
        x+=1
        if(x==10):
            x=1
    print()