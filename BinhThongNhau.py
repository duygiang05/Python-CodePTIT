par = [i for i in range(100005)]
siz = [1] * 100005

def find(a) :
    if (par[a] != a) :
        par[a] = find(par[a])
    return par[a]

def union(a,b) :
    x = find(a)
    y = find(b)
    if x == y : return
    if siz[x] < siz[y] : x,y = y,x
    par[y] = x ; siz[x] += siz[y]

t = int(input())   
for i in range(t) :
    x,y,z = map(int,input().split())
    if(z == 1) : union(x,y)
    else :
        if find(x) != find(y) : print(0)
        else : print(1)
    