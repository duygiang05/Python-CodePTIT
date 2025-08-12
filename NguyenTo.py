import math

def ucln(x, y) :
    if y == 0 : 
        return x
    return ucln(y, x % y)

def nto(x) :
    for i in range(2,math.isqrt(x) + 1) :
        if x % i == 0 :
            return False
    return x > 1

n = int(input())

for i in range(0,n) :
    x = int(input())
    cnt = 0
    for j in range(1,x) :
        if ucln (j, x) == 1 :
            cnt += 1
    
    if nto(cnt) == True :
        print("YES")
    else :
        print("NO")