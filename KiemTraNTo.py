import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if not x % i : return False
    return x > 1 

n,m = map(int,input().split())

a = []

for i in range(n) :
    lis = list(map(int,input().split()))
    a.append(lis)

for i in range(n) :
    for j in range(m) :
        if nto(a[i][j]) : print(1,end=' ')
        else : print(0,end=' ')
    print()
    
