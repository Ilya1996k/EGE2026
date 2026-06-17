from math import *

a=open('27_A.txt').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].replace(',','.').split()
    x,y=a[i]
    x=float(x)
    y=float(y)
    a[i]=x,y

K1=[]
K2=[]
for t in a:
    x,y=t
    if y>15:
        K1.append(t)
    else:
        K2.append(t)
        
        
def center(K):
    mn=10**10
    c=0
    for t1 in K:
        sm=0
        for t2 in K:
            sm+= dist(t1,t2)
        if sm<mn:
            mn=min(mn,sm)
            c=t1
    return c
    
c1=center(K1)       
c2=center(K2)
print(c1)
print(c2)
Px=(c1[0]+c2[0])*10000
Py=(c1[1]+c2[1])*10000
print(Px)
print(Py)
