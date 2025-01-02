List=['cap','bottle','pencil','hello','movie']
for i in List:
    if(len(i)==6):
        print(i)
print("-------------------")
List=['cap','pencil','hello','movie']
print(max(List))
print(min(List))
print("-----------------------")
List=['cap','bottle','pencil','hello','movie']
print("before sorting:",List)
List.sort()
print("after sorting:",List)
List.reverse()
print(List)
