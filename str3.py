"""
    Traversing string elements
    using for and while loop
"""
s = "ABCDEFGH"
for i in s:
    print(i,end=" ")
print() 
for j in range(0,len(s),2):
    print(s[j],end=" ")
print()
N = 0
while N<len(s):
    print(s[N],end=" ")
    N = N + 1