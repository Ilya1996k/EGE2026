from re import *
s = open('24.txt').readline()
num = r'(?:(?:[1-9][0-9]*[02468])|[02468])'
putern = rf'{num}(?:[+*]{num})+'
a = findall(putern,s)
print(len(max(a, key = len)))


from re import *
s = open("24.txt").readline()
A = r"(?:(?:[1-9][0-9]*[12346789])|[12346789])"
B = r"(?:(?:[1-9][0-9]*[05])|[50])"
pat = rf"(?:[(]{A}[-+]{B}[)])+"
p = findall(pat, s)
print(len(max(p, key = len)))
