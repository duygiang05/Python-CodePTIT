import math

def nto(x) :
    for i in range (2, math.isqrt(x) + 1) :
        if x % i == 0 :
            return False
    return x > 1

def sumDigit(x) :
    ans = 0
    while x > 0 :
        ans += x % 10
        x //= 10
    return ans

t = int(input())
for i in range(t) :
    x,y = map(int ,input().split())
    if nto(sumDigit(math.gcd(x, y))) == True :
        print("YES")
    else :
        print("NO")
    