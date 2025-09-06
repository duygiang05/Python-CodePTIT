n,k = map(int,input().split())
a = list(map(str,input().split()))
s = set()

for h in a : s.add(h)

a = sorted(list(s))
x = [0] * 35

def Try(i,n,k) :
    for j in range(x[i - 1] + 1, n - k + 1 + i) :
        x[i] = j;
        if i == k :
            for f in range(1,k + 1) :
                print(a[x[f] - 1],end=' ')
            print()
        else : Try(i + 1,n,k)
        
n = len(a)
Try(1,n,k)