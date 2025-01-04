#concatenate
str1='hello '
str2='every one'
result=(str1 + str2)
print(result)
print("-----------------------")
#length of the string
str3="afternoon"
print(type(str3))
print(len(str3)) 
#conversion of the upper cases and lower cases
str1='okay janu'
s1=str1.upper()
print(s1)
str2="WELCOME"
s2=str2.lower()
print(s2)
#reverse of a string
str1='keyboard'
s1=str1[::-1]
print(s1) 
#accessing sub strings using slicing
str2='keyboard is very useful to learn typing'
s1=str2[:7]
print(s1)
s2=str2[8:25]
print(s2)
#accessing elemenets
str4='welcome there is a party'
print(str4[0])
print(str4[-1])
#starts with or not
string='may I come in '
s=string.startswith('m')
print(s)
#count the no of times
string1="hello i am the user .may i know who are you"
s=string1.count('a')
print(s)
#program to print every second character()
str1="hello"
print(str1[1])
#program to print index value of certain 
str7="hello"
r=str7.index('o')
print(r)
#program to check alphabets
s="hello"
result=s.isalpha()
print(result)
#program to find index
s="engineering college"
result=s.index("g")
print(result)
#progrma to find digit or not
s3="1234"
result=s3.isdigit()
print(result)
##program to replace the occurence of the all stings
#splittting the strings
s4="welcome madam"
r=s4.split()
print(r)
#join of the strings
s1="welcome to "
s2="the party"
r=s1. join(s2)
print(r)
str1='hey there hello'
sub='hey'
if sub in str1:
    print("exist")
else:
    print("not exist")
    