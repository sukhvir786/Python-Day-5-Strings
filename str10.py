"""
    Program to convert vowels
    into upper case
"""
s = input("Enter any String : ")
s1=""
V ='aeiou'
for i in s:
    if i in V:
        s1=s1+i.upper()
    else:
        s1=s1+i
print("Now the string is:\n",s1)