Num="123456"
#conversion of str to list
list_Num=list(Num)
print(Num)
print(list_Num)
Res=''
for i in list_Num:
    Res=i+Res
print(Res)
print("---------------------")
Num="5678"
list_Num=list(Num)
print(Num)
print(list_Num)
print(list_Num[::-1])

