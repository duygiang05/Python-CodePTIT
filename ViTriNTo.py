import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if not x % i : return False
    return x > 1

def check(x) :
    for i in range(len(x)) :
        if nto(i) != nto(int(x[i])) : return False
    return True

t = int(input())

for i in range(t) :
    s = input()
    if check(s) : print("YES")
    else : print("NO")
    