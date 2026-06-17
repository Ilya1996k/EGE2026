f=open('24.txt').readline()
mx = 0
L = -1
R = -1
countCD = 0
while True:
    if countCD <= 160:
        R += 1
        if R == len(f):
            break
        if f[R-1:R+1] == "CD":
            countCD += 1 
    else:
        L += 1
        if f[L:L+2] == "CD":
            countCD -= 1
    if countCD == 160:
        mx = max(mx,R-L) 
print(mx)
