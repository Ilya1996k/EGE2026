#НАЙТИ МОЩНОСТЬ АЛФАВИТА
from math import *
l = 115
n = 65536
for N in range(1, 1000000):
    i = ceil(log2(N))
    I = ceil(i * l / 8)
    if I * n >= 13824 * 1024:
        print(N)
        break

#НАЙТИ ДЛИНУ СЕРИЙНОГО НОМЕРА
from math import log2,ceil
n=10+52+52+1989
i=ceil(log2(n))
n=836
I=639*1024
for l in range(10**6):
    Ix=ceil((i*l)/8)
    if Ix*n<=I:
        print(l)

