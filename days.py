Months=int(input("enter a month number:"))
if(Months==4 or Months==6 or Months==9 or Months==11):
    print("no of days are 30")
elif(Months==2):
    print("no of days are 28 or 29")
elif(Months==1 or Months==3 or Months==5 or Months==7 or Months==8 or Months==10 or Months==12):
    print("no of days are 31")
else:
    print("in valid month number:")