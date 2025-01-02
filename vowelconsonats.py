str=input("enter the sting:")
Vowel_count=0
for i in str:
    if(i in('A','E','I','O','U','a','e','i','o','u')):
        Vowel_count=Vowel_count+1
print("vowel count is:",Vowel_count)
print("_________________________________")
str=input("enter athe string:")
Vowel_count=0
Const_count=0
for i in str:
    if(i in('A','E','I','O','U','a','e','i','o','u')):
        Vowel_count=Vowel_count+1
    else:
        Const_count=Const_count+1
print("no of vowels are:",Vowel_count)
print("no of the consonants are:",Const_count)