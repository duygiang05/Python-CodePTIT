t = int(input())
d = dict()

for i in range(t) :
    d.clear(); key ,val = 1e9,-1
    tmp = int(input())
    for j in range(tmp) :
        n = int(input())
        d[n] = d.get(n,0) + 1
    for x,y in d.items() :
        if val < y : 
            val = y; key = x
        elif val == y :
            if key > x : key = x
    print(key) 
