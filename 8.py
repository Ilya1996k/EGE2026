from itertools import *
k=0
for x in product('0123456789ABC',repeat=6):
    s=''.join(x)
    if s[0]!='0':
        if s.count('111')==1 or s.count('333')==1 or s.count('555')==1 or s.count('777')==1 or s.count('999')==1 or s.count('BBB')==1:
            s=s.replace('1','*').replace('3','*').replace('5','*').replace('7','*').replace('9','*').replace('B','*')
            if s.count('*')==3:
                k+=1
print(k)
            
