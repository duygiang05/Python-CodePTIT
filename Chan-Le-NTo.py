import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if(not x % i) : return False
    return x > 1


def sumx(x) :
    ans = 0
    for i in x :
        ans += int(i)
    return ans
    
def check(x) :
    for i in range(len(x)) :
        tmp = int(x[i])
        if tmp % 2 != i % 2 : return False
    return True

t = int(input())
for i in range(t) :
    s = int(input())
    x = sumx(str(s))
    if(nto(x) and check(str(s))) : print("YES")
    else : print("NO")
    