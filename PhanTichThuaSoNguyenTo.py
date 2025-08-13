import math
def ptich(x) :
    s = ""
    for i in range (2,math.isqrt(x) + 1) :
        cnt = 0
        if x % i == 0 :
            while x % i == 0 :
                cnt += 1
                x //= i
            s += " * " + str(i) + "^" + str(cnt)
    if x > 1 : s += " * " + str(x) + "^" + "1"
    return s
 
t = int(input())

for i in range(t) :
    x = int(input())
    print("1" + ptich(x))