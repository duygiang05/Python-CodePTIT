t = int(input())

for i in range(t) :
    n = int(input())
    cnt = 1 if (n % 2) else 2
    ans = 0
    for i in range(cnt,n + 1,2) :
        ans += float(1) / i
    print("%.6f" % ans)