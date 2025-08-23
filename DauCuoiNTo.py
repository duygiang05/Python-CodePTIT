import math

def nto(x) :
    for i in range(2, math.isqrt(x) + 1) :
        if not x % i : return False
    return x > 1

t = int(input())

for i in range(t) :
    n = input()
    s1 = n[:3]
    s2 = n[len(n) - 3:]
    if nto(int(s1)) and nto(int(s2)) : print("YES")
    else : print("NO")