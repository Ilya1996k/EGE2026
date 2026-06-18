f = open('26.txt')

N = int(f.readline())
K = int(f.readline())
a = []

for s in f:
    t, c, s = s.split()
    c, s = int(c), int(s)
    a.append([t,c,s])

a.sort()
server = 0
backup = []
d = [0]*1_000_000
for t,c,s in a:
    d[c]+=s
    server+=s
    if server>K:
        if int(t[:2])<12: backup.append(server-s)
        server = s
backup.sort()
print(d.index(max(d)), backup[-1]+backup[-2])
