#Произведение двух простых чисел не обязательно различных
def p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def f(n):
    m=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if p(i)==True:
                m.append(i)
            if p(n//i)==True:
                m.append(n//i)
    return sorted(m)
c=0
for i in range(1324728,2000000):
    r=f(i)
    if len(r)==2:
        if r[0]*r[1]==i:
            if str(r[0]).count("5")==1 and str(r[1]).count("5")==1:
                print(i,max(r))
                c+=1
                if c==5:
                    break

#Произведение трех различных простых чисел 
def p(n):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True
def f(n):
    a = set()
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            if p(d):
                a.add(d)
            if p(n//d):
                a.add(n//d)
    return sorted(a)
k = 0 
for i in range(8930000-1, 1, -1):
    r = f(i)
    if len(r) == 3 and r[0] * r[1] * r[2] == i:
        if (str(r[0]).count("3") >= 1) + (str(r[1]).count("3") >= 1) + (str(r[2]).count("3") >= 1) == 1:
            print(i, r)
            k+=1
            if k == 5:
                break

#Маски

from fnmatch import*
for i in range(9874,10**10,9874):
    if fnmatch(str(i),"89*6?7?9?"):
        print(i,i//9874)


    
