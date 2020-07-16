"""
    Write a mirror function
    which takes two words as arguments
    and returns new word in the format
    w1w2:w2w1
"""
def FUN(w1,w2):
    print("1st String:",w1)
    print("2nd String:",w2)
    print("Mirror:")
    return w1+w2+":"+w2+w1
print(FUN("Hello","Python"))