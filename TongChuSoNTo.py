import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if not x % i : return False
    return x > 1

t = int(input()) 

for i in range(t) :
    n = int(input())
    ans = 0
    while n > 0 :
        ans += n % 10
        n //= 10
    if nto(ans) : print("YES")
    else :print("NO")