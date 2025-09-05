import math

l,r = map(int,input().split())

for i in range(l,r - 1) :
    for j in range(i,r ) :
        for k in range(j, r + 1) :
            if math.gcd(i,j) == 1 and math.gcd(j,k) == 1 and math.gcd(i,k) == 1 :
                t = (i,j,k) 
                print(t) 