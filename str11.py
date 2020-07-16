"""
    Program to delete vowels from the string
"""
def FUN(sentence):
    new = ""
    print("String : ",sentence)
    print("New String : ")
    for i in sentence:
        if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":
            new = new + i
    return new
print(FUN("i love python"))
        