a=open("17.txt").readlines()
for i in range(len(a)):
    a[i]=int(a[i])
mn=1000000000
for i in range(len(a)):
    if a[i]%23==0:
        mn=min(mn,a[i])
k=0
mxs=0
for i in range(len(a)-1):
    if a[i]%mn==0 or a[i+1]%mn==0:
        k+=1
        mxs=max(mxs,a[i]+a[i+1])
print(mxs,g)
