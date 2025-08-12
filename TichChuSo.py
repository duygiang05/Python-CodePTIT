def tich(x) :
    res = 1
    while x > 0 :
        if x % 10 != 0 :
            res *= x % 10
        x //=10
    return res
        

n = int(input())

while n > 0 :
    x = int(input())
    print(tich(x))
    n -= 1
    