t = int(input()) 

for i in range(t) :
    n = int(input())
    ans = 0
    while n > 0 :
        ans += n % 10
        n //= 10
    if ans > 10 and str(ans) == str(ans)[::-1] : print("YES")
    else : print("NO")