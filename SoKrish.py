def giaithua(x) :
    sum = 0 
    for h in x:
        tmp = int(h) ; ans = 1
        for j in range(1,tmp + 1) :
            ans *= j
        sum += ans
    return sum

t = int(input())
for i in range(t) :
    n = input()
    x = giaithua(n)
    if x == int(n) : print("Yes")
    else : print("No")