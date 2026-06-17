def f(n):
    alf = "0123456789AB"
    r = ""
    while n > 0:
        ost = n % 12
        r = alf[ost] + r
        n //= 12
    return r
a = [] 
for n in range(1,1000):
    r = f(n)
    if n % 4 == 0:
        r = "A" + r + "B"
    else:
        r = "1" + r + "0"
    r = int(r,12)
    if r > 2025:
        a.append(r)
print(min(a))
