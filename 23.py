def f(a,b):
    if a == 20 or a == 33:
        return 0
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return f(a+3,b) + f(a+4,b) + f(a*2,b)
print(f(3,15)*f(15,63) + f(3,26)*f(26,63) - f(3,15)*f(15,26)*f(26,63))
