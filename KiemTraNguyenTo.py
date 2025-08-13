import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if x % i == 0 : return False
    return x > 1

t = int(input())
for i in range(t) :
    s = input()
    x = s[len(s) - 4:]
    if not nto(int(x)) :
        print("NO")
    else :
        print("YES")