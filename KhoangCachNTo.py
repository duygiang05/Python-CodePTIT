import math

a = [0] * 8000

def sang() :
    a[0] = a[1] = 1
    for i in range(2,1000) :
        if not a[i] :
            for j in range(i * i, 8000, i) :
                a[j] = 1

n, x = map(int,input().split())
sang()
b = []
    
for i in range(8000) :
    if a[i] == 0:
        b.append(i)

for i in range(n + 1) :
    print(x ,end=' ')
    x += b[i]
    