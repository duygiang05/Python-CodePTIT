a,k,n = map(int,input().split()) ; 

tmp = (k + a - 1) // k * k
if tmp == a : tmp += k
b = tmp - a

if a + b > n : print(-1)
else :
    while a + b <= n :
        print(b,end=' ')
        b += k

