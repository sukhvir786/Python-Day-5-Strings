"""
Definition:
    Strings are treated as arrays of characters
    But in Python
    A String is an object of the str class
    This class has many constructors
"""
s1 = str()
print(s1)
s2 = str("STRINGS")
print(s2)
s3 = "STRINGS"
#s2 and s3 are equivalent
print(s3)
# Some inbuilt functions
print(len(s3))
print(min(s3))#it picks ascii value
print(max(s3))
