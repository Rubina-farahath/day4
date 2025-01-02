N=int(input("enter a number;"))
for i in range(N+1):
    print(i)
print("---------")
N=int(input("enter a number:"))
for i in range(N+1):
    print(i**2)
print("_________")
N=int(input("enter a number:"))
print("even numbers :")
for i in range(1,N+1):
    if(i%2==0):
        print(i)
        