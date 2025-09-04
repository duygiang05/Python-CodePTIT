t = int(input())
for i in range(t) :
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(); b.sort()
    l , check = 0, True
    while l < n :
        if a[l] > b[l] : 
            check = False; break
        l += 1
    print("YES") if check else print("NO")