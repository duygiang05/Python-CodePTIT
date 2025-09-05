n,m,x = map(int,input().split())
par = [0] * (n + 1)
siz = [1] * (n + 1)

for i in range(n + 1) :
    par[i] = i

def find(x) :
    if x != par[x] :
        par[x] = find(par[x]) 
    return par[x]

def union(u,v) :
    a,b = find(u) , find(v) 
    if a == b : return
    if a < b : a,b = b,a
    par[b] = a; siz[a] += siz[b]
    
for i in range(m) :
    u,v = map(int,input().split())
    union(u,v)
    
check = False
for i in range(1,n + 1) :
    if par[i] != par[x] : print (i); check = True

if not check : print(0)