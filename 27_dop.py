#A

from math import dist
def center(K):
    c=0
    mns=10**20
    for t1 in K:
        sm=0
        for t2 in K:
            sm+=dist(t1[:-1],t2[:-1])
        if sm<mns:
            mns=sm
            c=t1
    return c
a=open('27_A.txt').readlines()
for i in range(len(a)):
    a[i]=a[i].split()
    a[i][0]=float(a[i][0])
    a[i][1]=float(a[i][1])
K1=[]
K2=[]
for t in a:
    x,y,z=t
    if y<15:K1.append(t)
    if y>15:K2.append(t)
print(len(K1),len(K2))
C1=center(K1)
C2=center(K2)
print(C1,C2)
mn=10**20
Ax=0
Ay=0
for t in a:
    x,y,z=t
    if z=='VII':
        if dist(t[:-1],C1[:-1])<mn:
            mn=dist(t[:-1],C1[:-1])
            Ax=x
            Ay=y
print(Ax*10000)
print(Ay*10000)


#B

from math import dist
def center(k):
    b = []
    for t1 in k:
        s = 0
        for t2 in k:
            s += dist(t1[:-1], t2[:-1])
        b.append((s, t1))
    return min(b)[1]
a = open("1_27_B_97YhRPw (1).txt").readlines()
for i in range(len(a)):
    x, y, z = a[i].replace(",", ".").split()
    a[i] = [float(x), float(y), z]
k1, k2, k3= [], [], []
for t in a:
    x, y, z = t
    if y < 30:k1.append(t)
    if x > 16:k2.append(t)
    if y > 30 and x < 16:k3.append(t)
c1, c2, c3 = center(k1), center(k2), center(k3)
print(len(k1),len(k2), len(k3), len(a))
co1 = 0
co2 = 0
co3 = 0
for t1 in k1:
    x,y,z = t1
    if z == "G4IV":
        co1+=1
for t1 in k2:
    x,y,z = t1
    if z == "G4IV":
        co2+=1

for t1 in k3:
    x,y,z = t1
    if z == "G4IV":
        co3+=1
B1 = dist(c2[:-1], c3[:-1])
B2 = 0
for t1 in k1:
    if t1[2] == "O9V":
        for t2 in k1:
            if t2[2] == "O9V":
                B2 = max(B2, dist(t1[:-1], t2[:-1]))
for t1 in k2:
    if t1[2] == "O9V":
        for t2 in k2:
            if t2[2] == "O9V":
                B2 = max(B2, dist(t1[:-1], t2[:-1]))
for t1 in k3:
    if t1[2] == "O9V":
        for t2 in k3:
            if t2[2] == "O9V":
                B2 = max(B2, dist(t1[:-1], t2[:-1]))
print(B1*10000)
print(B2*10000)
