n=int(input("enter the value:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+64),end="")
    print()
print("------------------------")
n=int(input("enter a value:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+64),end="")
    print()
