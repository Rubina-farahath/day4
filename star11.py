'''n=int(input("entera number:"))
for i in range(n,0,-1):
    print("*"*i)
print("-------------------")
n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(i):
        print(i,end="")
        
    print()
print("----------------------")'''
n=int(input("enter a number:"))
for i in range(n):
    for j in range(0,n,-1):
        print(j,end="")
    print()