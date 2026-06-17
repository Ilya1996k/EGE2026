for a in range(1,3000):
    flag=True
    for x in range(1,3000):
        if ((x&117!=0) and (x&91==0)) <=(not(x&a==0)):
            continue
        else:
            flag=False
            break
    if flag==True:
        print(a)
