import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if not x % i : return False
    return x > 1

t = int(input())

for i in range(t) :
    s = input()
    tmp = s[len(s) - 4:]
    if nto(int(tmp)) : print("YES")
    else : print("NO")