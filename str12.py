"""
    Write the function which takes two words
    as arguments and returns true if first word
    is reverse of the second
"""
def FUN(w1,w2):
    print("1st word:",w1)
    print("2nd word:",w2)
    if w1==w2[::-1]:
        return True
    else:
        return False
print(FUN("hello","olleh"))
print(FUN("1245","5421"))