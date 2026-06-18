a = open('26.txt').readlines()
K = int(a.pop(0))
N = int(a.pop(0))
for i in range(len(a)):
    a[i] = a[i].split()
    a[i][0] = int(a[i][0])
    a[i][1] = int(a[i][1])
print(K, N, a[:10])
a.sort()
okno = [0]*K
ct = 0
for x in a:
    start, end = x
    for i in range(len(okno)):
        if start > okno[i]:
            okno[i] = end
            ct += 1
            print(i+1)
            break
print(ct)

