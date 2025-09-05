import math

n,k = map(int,input().split())

st , en = 10 ** (k - 1),10 ** k - 1; cnt = 0

for i in range(st,en + 1) :
    if cnt == 10 : print(); cnt = 0
    if math.gcd(n,i) == 1 : 
        print(i,end=' ')
        cnt += 1