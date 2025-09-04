t = int(input())

for _ in range(t) :
    d = dict(); 
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n) : 
        d[a[i]] = d.get(a[i],0) + 1
    
    for x,y in d.items() :
        if y % 2 : print(x) ; break