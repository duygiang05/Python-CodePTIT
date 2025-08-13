import math

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if x % i == 0 : 
            return False
    return x > 1

def check(x) :
    cnt = 0
    for h in x :
        if h != "2" and h != "3" and h != "5" and h != "7" :
            cnt += 1
    if cnt >= len(x) - cnt :
        return False
    return True

t = int(input()) 
for i in range(t) :
    s = input()
    if nto(len(s)) and check(s) :
        print("YES")
    else :
        print("NO")