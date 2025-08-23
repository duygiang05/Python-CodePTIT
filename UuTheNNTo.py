import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1):
        if not x % i : return False
    return x > 1

t = int(input())

for i in range(t) :
    n = input()
    cnt = 0
    for h in n :
        if h in '2357' : cnt += 1
    if cnt > len(n) - cnt and nto(len(n)) : print("YES")
    else : print("NO")