t = int(input())

for i in range(t) :
    
    n = int(input())
    a = list(map(int,input().split()))
    d = dict()
    
    for h in a :
        d[h] = d.get(h,0) + 1
    key , val = 1e9, -1
    
    for x,y in d.items() :
        if y > n/2 :
            if y > val : val = y; key = x
            elif y == val : key = min(x,key)
            
    if val != -1 : print(key)
    else : print("NO")
            