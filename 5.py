def per(n):
    s=''
    while n!=0:
        s=str(n%7)+s
        n=n//7
    return s
for n in range(1,1000):
    r=per(n)
    sm=sum(int(x) for x in r)
    if sm%2==0:
        r=r+'555'
    else:
        r='33'+r+'6'
    r=int(r,7)
    if r<12717:
        print(n)
