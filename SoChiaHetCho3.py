def check(x) :
    sum = 0
    while x > 0 :
        sum += x %10
        x //=10
    return sum

n = int(input())

while n > 0 :
    x = int(input())
    
    if check(x) % 3 == 0 :
        print("YES")
    else :
        print("NO")
    n -= 1