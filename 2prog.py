from itertools import product,permutations
def f(x,y,z,w):
    return (z <= w) and y and (not x)
    
for x in product((0,1), repeat = 5):
    a1,a2,a3,a4,a5 = x
    s1 = (0,1,a1,0)
    s2 = (a2,0,a3,a4)
    s3 = (0,1,1,a5)
    if len(set([s1,s2,s3])) == 3:
        for r in permutations("xyzw"):
            if f(**dict(zip(r, s1))) == 1:
                if f(**dict(zip(r, s2))) == 1:
                    if f(**dict(zip(r, s3))) == 0:
                        print(*r)
