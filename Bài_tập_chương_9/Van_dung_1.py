def sign(x:int):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
print(sign(8))
print(sign(-8))
print(sign(0))