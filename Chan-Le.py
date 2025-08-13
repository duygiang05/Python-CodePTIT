import math

def sumDigit(x) :
    ans = 0 
    for h in x :
        ans += int(h)
    if ans % 10 == 0 : return True
    return False

def check (x) :
    for i in range(1,len(x) - 1) :
        if math.fabs((int(x[i]) - int(x[i - 1]))) != 2 :
            return False
    return True

t = int(input())

for i in range(t) :
    x = input()
    
    if sumDigit(x) and check(x) : 
        print("YES")
    else :
        print("NO")