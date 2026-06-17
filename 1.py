from itertools import *
s1 = "348 47 17 128 67 58 235 146"
s2 = "hf ga hcd gcb fd aeb fc egd"
s2 = {frozenset(x) for x in s2.split()}
print("1 2 3 4 5 6 7 8")
for x in permutations("abcdefgh"):
    s3 = s1
    for r in zip("12345678", x):
        a, b = r
        s3 = s3.replace(a, b)
    s3 = {frozenset(x) for x in s3.split()}
    if s3 == s2:
        print(*x)
