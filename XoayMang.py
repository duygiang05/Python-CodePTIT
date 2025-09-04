t = int(input())
for i in range(t) :
    n,d = map(int,input().split())
    a = list(map(int,input().split()))
    a = a[d:] + a[:d]
    for h in a :
        print(h,end=' ')
    print()