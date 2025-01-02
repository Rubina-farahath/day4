str=input("enter the string:")
str=str.lower()
str=str.replace(' ','')
vowel_count=0
const_count=0
for i in str:
    if(i in('a','e','i','o','u')):
        vowel_count=vowel_count+1
    elif(i.isalpha()):
        const_count=const_count+1
print("vowels count:",vowel_count)
print("consts are:",const_count)
print("--------------------------------------------")
str=input("enter the string:")
str=str.lower()
str=str.replace(' ','')
isalpha=0
isdigit=0
special_count=0
vowel_count=0
const_count=0
for i in str:
    if(i in('a','e','i','o','u')):
        vowel_count=vowel_count+1
    elif(i.isalpha()):
        const_count=const_count+1
    elif(i.isdigit()):
        isdigit=isdigit+1
    else:
        special_count=special_count+1
print("vowels count:",vowel_count)
print("consts are:",const_count)
print("digit count :",isdigit)
print("special count:",special_count)