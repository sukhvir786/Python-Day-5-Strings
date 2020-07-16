"""
    INDEX Operator:
        String is a sequence of characters
        which can be accessed one at a time
        The characters in the string are 0 based
        for example:
    STRING :  P  Y  T  H  O  N  P  R  O  S  
     INDEX :  0  1  2  3  4  5  6  7  8  9   
 -ve INDEX :-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
           : 
"""
s = "PYTHONPROS"
#s = "sukhvirsingh"
#s = "abcdefghijklmnopqrstuvwxyz"
n = len(s)
print(s)
print(s[0])
print(s[-1])
print(s[2])
print(s[1:7])
print(s[9:2:-1])
print(s[n::-1])