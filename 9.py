f=open('9.txt').readlines()
k=0
for i in f:
    i=i.split()
    i=list(map(int,i))
    i.sort()
    a1=[x for x in i if i.count(x)==2]
    a2=[x for x in i if i.count(x)==1]
    if len(a1)==2 and len(a2)==3:
        if i[0] not in a1 and i[4] not in a1:
            k+=1
print(k)
