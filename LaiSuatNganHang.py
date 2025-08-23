import math

t = int(input())

for i in range(t) :
    n , x , m = map(float,input().split())
    tmp = m / n
    print(math.ceil(math.log(tmp,1 + x / 100)))