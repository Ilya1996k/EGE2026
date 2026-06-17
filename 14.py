#1
alf = "0123456789ABCDEFGH"
for x in alf:
    a = int(f"11H{x}05", 18) + int(f"3F{x}54{x}8", 18) + int(f"G{x}{x}{x}9", 18)
    if a % 14 == 0:
        print(a // 14)
        break


#2
for x in range(0,40):
    a1=8*40**6 + 7*40**5 + 1*40**4 + x*40**3 + 2*40**2 + 9*40**1 + 1*40**0
    a2=3*40**6 + 6*40**5 + 6*40**4 + x*40**3 + 6*40**2 + 3*40**1 + 1*40**0
    a3=9*40**6 + 7*40**5 + 3*40**4 + x*40**3 + 6*40**2 + 1*40**1 + 8*40**0
    s=a1+a2+a3
    if s%39==0:
        print(s/13)
#3
def f(n):
    r = []
    while n > 0:
        r.append(n % 16)
        n //= 16
    return r[::-1]

a = 2*16**2020 + 9*16**2021 - 2*4**2022 + 8**2023 - 2*2**2024 - 65536
r = f(a)
k = 0
for x in r:
  if x > 9:
    k += 1
print(k)

#4
def f(n):
    r = []
    while n != 0:
        r.append(n%27)
        n = n // 27
    return r[::-1]
for x in range(1, 27000):
      a = 3 * 27**9 + 2 * 27**6 + 27**3 - x
      b = f(a)
      if b.count(0) == 6:
          print(x)
