def f(a, b):
    if a < b: return 0
    if a == b: return 1
    if a > b:
        if str(a)[-2] > str(a)[-1]:
            a1 = int(str(a)[:-2] + str(a)[-1] + str(a)[-2])
            return f(a1, b) + f(a-3, b)
        else:
            return f(a-3, b)
print(f(1001,959)*f(959,902))
