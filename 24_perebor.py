#1
s=open("24.txt").readline()
n=len(s)
mx=1
for i in range(n):
    for j in range(i+mx,n):
        sr=s[i:j+1]
        if sr.count("BC")==190:
            mx=max(mx,len(sr))
        if sr.count("BC")>190:
            break
print(mx)

#2
s = open("24.txt").readline()
mn = 100000000
for i in range(len(s)):
    if s[i] in "AEIOUY":
        for j in range(i+1, len(s)):
            if s[j] in "AEIOUY":
                break
            sr = s[i:j+1]
            if sr.count("20") == 26:
                mn = min(mn, len(sr))
            if sr.count("20") > 26:
                break
print(mn)

#3

f = open('24.txt').readline()

mx = 1
for i in range(len(f)):
    for j in range(i+mx, len(f)):
        s = f[i:j+1]
        if s.count('2025') >= 90 and s.count('Y') == 80:
              mx = max(mx, len(s))
        if s.count('Y') > 80:
            break
print(mx)  
        
