n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+96),end="")
    print()