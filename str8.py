"""
    Testing strings:
        String may containg 
        lower case, upper case, digits, alphabets,
        both digits & alphabets etc.
        these can be tested using
        1. isalnum
        2. isalpha
        3. isdigit
        4. islower
        5. isupper
        6. isspace
"""
s1 = "abc123"
print(s1.isalnum())
s2 = "123"
print(s2.isdigit())
s3 = "abc"
print(s3.isalpha())
s4 = "sukhvir"
print(s4.islower())
s5 = "SUKHVIR"
print(s5.isupper())
s6 = " "
print(s6.isspace())


