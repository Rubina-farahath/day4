n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(n):
        print(i,'',end="")
    print()
print("----------------------------")
n=int(input("enter a number :"))
for i in range(n):
    for j in range(n,0,-1):
        print(j,"",end="")
    print()
print("-------------------")
n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(n):
        print(chr(i+64),"",end="")
    print()
print("---------------------------")
n=int(input("enter a number:"))
for i in range(n):
    for j in range(n,0,-1):
        print(chr(j+64),"",end="")
    print()
print("-------------------")
n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(n):
        print(chr(i+96),"",end="")
    print()
print("---------------------------")
n=int(input("enter a number:"))
for i in range(n):
    for j in range(n,0,-1):
        print(chr(j+96),"",end="")
    print()
print("---------------------------")

    
    

