n=int(input("entera number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
      if(j%2==0):
         print(0,end="")
      else:
         print(1,end="")
    print()
print("----------------------")
n=int(input("entera number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
      if(i%2==0):
         print(0,end="")
      else:
         print(1,end="")
    print()