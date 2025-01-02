std=input("enter student name:")
sub1=int(input("sub1 score:"))
sub2=int(input("sub2 score:"))
sub3=int(input("sub3 score:"))
total=0
avg=0
print("student report:")
print("-------------")
print("student name:",std)
print("subject1:",sub1)
print("subject1:",sub2)
print("subject1:",sub3)
if(sub1>=35 and sub2>=35 and sub3):
    total=sub1+sub2+sub3
    print("Total:",total)
    avg=total/3
    print("Average:",avg)
    if(avg>=90):
        print("congratulations you have passed in 1st class:")
    elif(avg>=75):
        print("congratulations you have passed in 2nd class:")
    else:
        print("congratulations you have passed in 3rd class:")
else:
    print("better luck next time:")
    