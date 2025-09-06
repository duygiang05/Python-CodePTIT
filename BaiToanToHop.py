n,k = map(int,input().split())

a = list(map(int,input().split()))
s = set()
x = [0] * 30

for h in a :
    s.add(h)

a = sorted(list(s))

def Try(i,n,k) :
    for j in range(x[i - 1] + 1,n - k + i + 1) :
        x[i] = j
        if i == k :
            for f in range(1,k + 1) :
                print(a[x[f] - 1],end=' ')
            print() ; 
        else : Try(i + 1,n,k)
        

Try(1,len(a),k)