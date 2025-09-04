import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if not x % i : return False
    return x > 1

n = int(input())

a = list(map(int,input().split()))
d = dict()

for x in a :
    if nto(x) :
        d[x] = d.get(x,0) + 1

for x,y in d.items() :
    print(x,y,sep = ' ',end = '\n')
