N=int(input("enter a numberL::"))
print("even numbers are")
for i in range(2,N+1,2):
    print(i)
print("____________")
N=int(input("enter a number:"))
print("odd numbers are:")
for i in range(1,N+1):
        if(i%2!=0):
              print(i,end='')
print("-------")
N=int(input("enter a number:"))
print("multiples of",N)
for i in range(0,N):
      print(N,"X",i,"=",N*i)       
      